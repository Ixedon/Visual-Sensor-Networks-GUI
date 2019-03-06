from init import *

class MainWindow:
	def __init__(self, master):
		self.master = master
		self.master.title("VSN Camera GUI")
		self.master.wm_protocol("WM_DELETE_WINDOW", self.OnClose)

		self.panel = []
		self.texts = []
		self.sockets = []
		self.k = 0
		self.f = 0
		self.threadID = 0
		self.oldimage = None

		self.thread = None
		self.stopEvent = None

		self.InitUI()
		self.InitConnection()
	
		self.StartVideo()

	def InitUI(self):
		
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

		VideoFrame.pack()
		

		self.close_button = Button(self.master, text="Close", command=self.OnClose)
		self.close_button.pack()

	def StartVideo(self):
		for x in range(0,5):
			self.stopEvent = threading.Event()
			self.thread = threading.Thread(target=self.VideoLoop, args=())
			self.thread.start()

	def VideoLoop(self):
		cameraID = self.threadID
		self.threadID = self.threadID + 1
		print ("thread ready: " + str(cameraID + 1))
		
		while not self.stopEvent.is_set():
			try:
				image = self.GetImage(cameraID)
			except AttributeError:
				pass                   # error on quiting

			try:

				if image != None:
					self.panel[cameraID].configure(image = image)
					self.panel[cameraID].image = image
			except AttributeError:
				pass                   # error on quiting						
			

	def OnClose(self):
			
			for socket in self.sockets:
				try:
					socket.close()
				except:
					pass
			self.stopEvent.set()
			self.master.quit()

	def GetImage(self, cameraID):
		if len(self.sockets) <= cameraID:
			return None

		socket = self.sockets [cameraID]
		image = None
		try:
			string = socket.recv_multipart(2)
		except zmq.error.ZMQError:
			return None                      

		if (string[0].decode("utf-8")=="Image"):
			msg=ImageInfo()
			msg.ParseFromString(string[1])
			 
			image_data=msg.image

			image = Image.frombytes('RGB', (640,480), image_data)  # to PIL
			
			if msg.bbHeight > 0:
				image = numpy.array(image)     # to cv2 format

				cv2.rectangle( image, (msg.bbX, msg.bbY), (msg.bbX + msg.bbWidth, msg.bbY + msg.bbHeight), (255, 0, 255), 2, 8, 0 )  #bounding box
				

				image = Image.fromarray(image)   # back to PIL
			
			b,g,r=image.split()               # convert BGR to RGB
			image=Image.merge("RGB", (r,g,b))

			image = image.resize((320,240))  

			image = ImageTk.PhotoImage(image)
			self.texts[cameraID].set("[Camera " + str(cameraID + 1)+ "]: No message")

		elif (string[0].decode("utf-8")=="Command"):
			cmd = AdditionalControl()
			cmd.ParseFromString(string[1])
			self.texts[cmd.cameraID - 1].set(cmd.command)
			
		return image
			


	def InitConnection(self):

		context = zmq.Context.instance()

		for x in range(1,6):
			socket = context.socket(zmq.SUB)
			socket.setsockopt(zmq.LINGER, 100)
			print("CONNECTED " + str(x))
			socket.connect("tcp://192.168.1.15"+str(x)+":9000")   # for lab network
			#socket.connect("tcp://127.0.0.1"+str(x)+":9000")       # for local webcam testing
			socket.subscribe("")
			self.sockets.append(socket)
		
