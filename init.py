import zmq, io, numpy, sys, cv2, time, base64
import threading, datetime, imutils
from tkinter import Tk, Label, Button, Canvas, NW, Frame, StringVar
from PIL import Image, ImageTk, ImageDraw
from Message_pb2 import ImageInfo, AdditionalControl