from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from main import execute

class ezFOAM(Tk):

    dim = None
    flow = None
    bound = None
    cores = None

    def __init__(self):
        super(ezFOAM, self).__init__()
        self.title("ezFOAM")
        self.minsize(640, 400)

        self.intro = ttk.Label(self, text = "Answer all the questions below and select Build Case for fast simulation set-up")
        self.intro.grid(row = 0)

        self.destinationFrame = ttk.LabelFrame(self, text = "Select simulation destination")
        self.destinationFrame.grid(row = 1, column = 0, sticky = W, padx = 1)
        self.destinationButton()

        self.browseFrame = ttk.LabelFrame(self, text = "Select su2 geometry file")
        self.browseFrame.grid(row = 1, column = 2, sticky = E, padx = 1)
        self.browseButton()

        self.unitFrame = ttk.LabelFrame(self, text = "Specify inlet flow rate and units")
        self.unitFrame.grid(row = 2, column = 0, sticky = W, padx = 1)
        self.flowRateEntry()
        self.flowRateButton()        
        self.velocityButton()
        self.volFlowRateButton()

        self.flowTypeFrame = ttk.LabelFrame(self, text = "Specify flow type")
        self.flowTypeFrame.grid(row = 2, column = 2, sticky = E, padx = 1)
        self.airButton()
        self.waterButton()
        self.multiphaseButton()

        self.boundFrame = ttk.LabelFrame(self, text = "Is the flow internal or external?")
        self.boundFrame.grid(row = 3, column = 2, sticky = E, padx = 1)
        self.trisurfaceButton()
        self.blockmeshButton()

        self.coreFrame = ttk.LabelFrame(self, text = "Enter the number of processor cores you wish to use (1 or more)")
        self.coreFrame.grid(row = 3, column = 0, sticky = W, padx = 1)
        self.coreEntry()
        self.coreButton()

        self.thetaFrame = ttk.LabelFrame(self, text = "Enter the desired angle of attack ranging from -30 degrees to 30 degress")
        self.thetaFrame.grid(row = 4, column = 0, sticky = W, padx = 1)
        self.thetaEntry()
        self.thetaButton()

        self.turbulentFrame = ttk.LabelFrame(self, text = "Is the flow laminar or turbulent?")
        self.turbulentFrame.grid(row = 4, column = 2, sticky = E, padx = 0)
        self.laminarButton()
        self.turbulentButton()

        self.buildFrame = ttk.LabelFrame(self)
        self.buildFrame.grid(row = 5, column = 0, sticky = W, padx = 1)
        self.buildButton()

    def destinationButton(self):
        self.destinationButton = ttk.Button(self.destinationFrame, text = "Browse", command = self.browsePath)
        self.destinationButton.grid(row = 1, column = 1)

    def browseButton(self):
        self.browseButton = ttk.Button(self.browseFrame, text = "Browse", command = self.fileDialog)
        self.browseButton.grid(row = 1, column = 1)

    def velocityButton(self):
        self.velocityButton = ttk.Button(self.unitFrame, text = "m/s")
        self.velocityButton.grid(row = 2, column = 2)
        self.velocityButton.bind("<Button-1>", self.velocityButtonFunc)

    def volFlowRateButton(self):
        self.volFlowRateButton = ttk.Button(self.unitFrame, text = "m3/s")
        self.volFlowRateButton.grid(row = 2, column = 3)
        self.volFlowRateButton.bind("<Button-1>", self.volFlowRateButtonFunc)

    def airButton(self):
        self.airButton = ttk.Button(self.flowTypeFrame, text = "Air Steady")
        self.airButton.grid(row = 2, column = 0)
        self.airButton.bind("<Button-1>", self.airButtonFunc)

    def waterButton(self):
        self.waterButton = ttk.Button(self.flowTypeFrame, text = "Water Steady")
        self.waterButton.grid(row = 2, column = 1)
        self.waterButton.bind("<Button-1>", self.waterButtonFunc)

    def multiphaseButton(self):
        self.multiphaseButton = ttk.Button(self.flowTypeFrame, text = "Multiphase")
        self.multiphaseButton.grid(row = 2, column = 2)
        self.multiphaseButton.bind("<Button-1>", self.multiphaseButtonFunc)
  
    def trisurfaceButton(self):
        self.trisurfaceButton = ttk.Button(self.boundFrame, text = "Internal")
        self.trisurfaceButton.grid(row = 3, column = 0)
        self.trisurfaceButton.bind("<Button-1>", self.trisurfaceButtonFunc)

    def blockmeshButton(self):
        self.blockmeshButton = ttk.Button(self.boundFrame, text = "External")
        self.blockmeshButton.grid(row = 3, column = 1)
        self.blockmeshButton.bind("<Button-1>", self.blockmeshButtonFunc)

    def thetaEntry(self):
        self.thetaEntry = ttk.Entry(self.thetaFrame)
        self.thetaEntry.grid(row = 4, column = 0, sticky = E)

    def thetaButton(self):
        self.thetaButton = ttk.Button(self.thetaFrame, text = "Enter")
        self.thetaButton.grid(row = 4, column = 1)
        self.thetaButton.bind("<Button-1>", self.thetaButtonFunc)

    def coreEntry(self):
        self.coreEntry = ttk.Entry(self.coreFrame)
        self.coreEntry.grid(row = 3, column = 0, sticky = E)

    def flowRateEntry(self):
        self.flowRateEntry = ttk.Entry(self.unitFrame)
        self.flowRateEntry.grid(row = 2, column = 0, sticky = W)

    def coreButton(self):
        self.coreButton = ttk.Button(self.coreFrame, text = "Enter")
        self.coreButton.grid(row = 3, column = 1)
        self.coreButton.bind("<Button-1>", self.coreButtonFunc)

    def flowRateButton(self):
        self.flowRateButton = ttk.Button(self.unitFrame, text = "Enter")
        self.flowRateButton.grid(row = 2, column = 1)
        self.flowRateButton.bind("<Button-1>", self.flowRateButtonFunc)

    def buildButton(self):
        self.buildButton = ttk.Button(self, text = "Build OpenFOAM Case")
        self.buildButton.grid(row = 5, column = 0, sticky = W)
        self.buildButton.bind("<Button-1>", self.buildButtonFunc)

    def laminarButton(self):
        self.laminarButton = ttk.Button(self.turbulentFrame, text = "Laminar")
        self.laminarButton.grid(row = 4, column = 0, sticky = E)
        self.laminarButton.bind("<Button-1>", self.laminarButtonFunc)  

    def turbulentButton(self):
        self.turbulentButton = ttk.Button(self.turbulentFrame, text = "Turbulent")
        self.turbulentButton.grid(row = 4, column = 1, sticky = E)
        self.turbulentButton.bind("<Button-1>", self.turbulentButtonFunc) 

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select A SU2 File", filetype = (("SU2 Files", "*.su2"), ("All Files", "*.*")))
        self.file_label = ttk.Label(self.browseFrame, text = "")
        self.file_label.grid(column = 2, row = 1, sticky = W)
        self.file_label.configure(text = self.filename)

    def browsePath(self):
        self.pathname = filedialog.askdirectory()
        self.path_label = ttk.Label(self.destinationFrame, text = "")
        self.path_label.grid(column = 2, row = 1, sticky = W)
        self.path_label.configure(text = self.pathname)
        

    def velocityButtonFunc(self,event):
        self.dim = 0

    def volFlowRateButtonFunc(self,event):
        self.dim = 1
    
    def airButtonFunc(self,event):
        self.flow = 0

    def waterButtonFunc(self,event):
        self.flow = 1

    def multiphaseButtonFunc(self,event):
        self.flow = 2

    def trisurfaceButtonFunc(self,event):
        self.bound = 0

    def blockmeshButtonFunc(self,event):
        self.bound = 1

    def laminarButtonFunc(self,event):
        self.turbulence = 0

    def turbulentButtonFunc(self,event):
        self.turbulence = 1
    
    def coreButtonFunc(self,event):
        self.cores = int(self.coreEntry.get())

    def flowRateButtonFunc(self,event):
        self.inletU = str(self.flowRateEntry.get())

    def thetaButtonFunc(self,event):
        self.theta = str(self.thetaEntry.get())
    
    def buildButtonFunc(self,event):
        execute(self.pathname, self.filename, self.dim, self.flow, self.inletU, self.bound, self.cores, self.theta, self.turbulence)
        messagebox.showinfo("Notice", "Process complete")
        #make a widget that takes value of flow 
       
root = ezFOAM()
root.mainloop()
