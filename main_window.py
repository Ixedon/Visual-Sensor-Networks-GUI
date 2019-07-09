from init import *

class MainWindow:
    def __init__(self, master, local, ncam):
        # Initialize variables and settings

        self.local = local # local or lab usage
        self.ncam = ncam # maximum ammount of cameras
        self.master = master
        self.master.title("VSN Camera GUI")
        self.master.wm_protocol("WM_DELETE_WINDOW", self.OnClose)

        self.panel = []
        self.texts = []
        self.sockets = []
        self.anti_flicker_counter = []
        self.pred = StringVar()
        self.threadID = 0

        self.thread = None
        self.stopEvent = None

        # Run program
        self.InitUI()
        self.InitConnection()
    
        self.StartVideo()

    def InitUI(self):
        #Create the UI
        self.pred.set("No shape")
        Prediction = Label(self.master, textvar = self.pred)
        Prediction.pack()

        VideoFrame = Frame(self.master)

        for x in range(0,2):
            for y in range(0,3):
                frm = Frame(VideoFrame)
                pnl = Label(frm,image = None)
                pnl.image = None
                pnl.pack()

                textvar = StringVar()
                textvar.set("")
                txt = Label(frm, textvar = textvar)
                txt.pack()
                frm.grid(row = x, column = y)
                self.panel.append(pnl)
                self.texts.append(textvar)
                self.anti_flicker_counter.append(0)

        VideoFrame.pack()
        

        self.close_button = Button(self.master, text="Close", command=self.OnClose)
        self.close_button.pack()

    def StartVideo(self):
        # Start the video threads
        for x in range(0,self.ncam):
            self.stopEvent = threading.Event()
            self.thread = threading.Thread(target=self.VideoLoop, args=())
            self.thread.start()

    def VideoLoop(self):
        # Run single video stream

        cameraID = self.threadID
        self.threadID = self.threadID + 1
        print ("thread ready: " + str(cameraID +1))
        
        while not self.stopEvent.is_set():
            try:
                image = self.GetImage(cameraID)
            except AttributeError:
                # Handle error on quiting
                pass

            try:

                if image != None:
                    self.panel[cameraID].configure(image = image)
                    self.panel[cameraID].image = image
            except AttributeError:
                # Handle error on quiting
                pass                                        
            

    def OnClose(self):
            # Exit application (clean up)
            for socket in self.sockets:
                try:
                    socket.close()
                except:
                    pass
            self.stopEvent.set()
            self.master.quit()

    def GetImage(self, cameraID):
        # Process new message

        # Check if socket exists
        if cameraID >= len(self.sockets) :
            return None

        # Receive image from ZMQ
        socket = self.sockets [cameraID]
        image = None
        try:
            string = socket.recv_multipart()
        except zmq.error.ZMQError:
            return None                      


        # Process when message is an image
        if (string[0].decode("utf-8")=="Image"):
            msg=ImageInfo()
            
            try:
                msg.ParseFromString(string[1])
            except DecodeError:
                return None

            image_data=msg.image

            # Convert to PIL format
            image = Image.frombytes('RGB', (640,480), image_data)  
            
            # Convert to to cv2 format
            image = numpy.array(image)

            # Number the streams
            cv2.putText(image,str(cameraID + 1), (10,70),cv2.FONT_HERSHEY_TRIPLEX, 3, (0,200,0),2)

            # Add bouding box if it exists
            if msg.bbHeight > 0:
                cv2.rectangle( image, (msg.bbX, msg.bbY), (msg.bbX + msg.bbWidth, msg.bbY + msg.bbHeight), (255, 0, 255), 2, 8, 0 )  #bounding box
            
            # Convert back to PIL
            image = Image.fromarray(image)
            
            # Convert from BGR to RGB
            b,g,r=image.split()
            image=Image.merge("RGB", (r,g,b))

            image = image.resize((320,240))  

            # Convert to TK format
            image = ImageTk.PhotoImage(image)

            # Make sure the change is longer so it doesn't flicker
            if self.anti_flicker_counter[cameraID] > 30:
                self.texts[cameraID].set("No message")
                self.anti_flicker_counter[cameraID] = 0
            else:
                self.anti_flicker_counter[cameraID] +=1

        # Process when message is an text command
        elif (string[0].decode("utf-8")=="Command"):
            cmd = AdditionalControl()

            try:
                cmd.ParseFromString(string[1])
            except DecodeError:
                pass
            
            # Set the camera's command string   
            self.texts[cmd.cameraID - 1].set(cmd.command)
            self.anti_flicker_counter[cameraID] = 0

        # Process when message is a predicion from a leader
        elif (string[0].decode("utf-8")=="Prediction"):
            cmd = AdditionalControl()
            
            try:
                cmd.ParseFromString(string[1])
            except DecodeError:
                pass

            #update the predition text on the top of the interface
            self.pred.set(cmd.command)
            
        return image
            


    def InitConnection(self):
        # Initialize the ZMQ connection

        context = zmq.Context.instance()

        if not self.local:
            # Work in lab with cameras
           for x in range(1,self.ncam + 1):
                # Create and connect the sockets (publish on tcp://*:9000 or tcp://*:8000)
                socket = context.socket(zmq.SUB)
                print("CONNECTED " + str(x))
                socket.connect("tcp://192.168.1.15"+str(x)+":9000")
                socket.connect("tcp://192.168.1.15"+str(x)+":8000")
                
                # Subscribe to types of messages
                socket.subscribe("Image")
                socket.subscribe("Command")
                socket.subscribe("Prediction")

                # Make a list of all the sockets
                self.sockets.append(socket)
        else:
            # Work on local computer with webcam (publish on tcp://*:9000 or tcp://*:8000)
            socket = context.socket(zmq.SUB)
            socket.connect("tcp://127.0.0.1:9000")
            socket.connect("tcp://127.0.0.1:8000")
            
            # Subscribe to types of images
            socket.subscribe("Image")
            socket.subscribe("Command")
            socket.subscribe("Prediction")

            # Make a list of all the sockets
            self.sockets.append(socket)