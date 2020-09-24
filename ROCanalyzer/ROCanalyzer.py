import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from scipy.stats import gaussian_kde
import numpy as np

import random

class Window(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setWindowTitle('C-ROC analyzer')

        # a figure instance to plot on
        self.figurePDF = Figure()
        self.figureROC = Figure()

        self.xdata=[]
        self.ydata1=[]
        self.ydata2=[]

        self.plotroc=False

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvasROC = FigureCanvas(self.figureROC)
        self.sliderROC = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.sliderROC.setMinimum(0)
        self.sliderROC.setMaximum(100)
        self.sliderROC.setValue(50)
        self.sliderROC.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sliderROC.setTickInterval(5)
        self.sliderROC.valueChanged.connect(self.ROCvaluechanged)
        
        self.canvasPDF = FigureCanvas(self.figurePDF)
        self.sliderPDF = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.sliderPDF.setMinimum(0)
        self.sliderPDF.setMaximum(100)
        self.sliderPDF.setValue(50)
        self.sliderPDF.setTickPosition(QtWidgets.QSlider.TicksBelow)
        #self.sliderPDF.setTickInterval(1)
        self.sliderPDF.valueChanged.connect(self.PDFvaluechanged)
        
        
        # Just some button connected to `plot` method
        self.buttonPlotPdf = QtWidgets.QPushButton('Plot PDF')
        self.buttonPlotPdf.clicked.connect(self.readData)
        
        # Just some button connected to `plot` method
        self.buttonPlotRoc = QtWidgets.QPushButton('Plot ROC')
        self.buttonPlotRoc.clicked.connect(self.plotRoc)
        
        # Close button
        self.buttonClose = QtWidgets.QPushButton('Close')
        self.buttonClose.clicked.connect(self.close)

        # set the layout
        layout_outer =   QtWidgets.QVBoxLayout()
        layout_canvas =  QtWidgets.QHBoxLayout()
        layout_toolbar = QtWidgets.QHBoxLayout()
        layout_ROC = QtWidgets.QVBoxLayout()
        layout_PDF = QtWidgets.QVBoxLayout()

        layout_PDF.addWidget(self.canvasPDF)
        layout_PDF.addWidget(self.sliderPDF)
        layout_ROC.addWidget(self.canvasROC)
        layout_ROC.addWidget(self.sliderROC)
        layout_toolbar.addWidget(self.buttonPlotPdf)
        layout_toolbar.addWidget(self.buttonPlotRoc)
        layout_toolbar.addWidget(self.buttonClose)
        layout_canvas.addLayout(layout_PDF)
        layout_canvas.addLayout(layout_ROC)
        layout_outer.addLayout(layout_canvas)
        layout_outer.addLayout(layout_toolbar)
        
        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbarPDF = NavigationToolbar(self.canvasROC, self)
        self.toolbarROC = NavigationToolbar(self.canvasPDF, self)
        
        self.setLayout(layout_outer)

    def plotRoc(self):
        self.plotroc = not self.plotroc
        self.replot()
        
    def readData(self):
        N=100
        
        if len(sys.argv)>1:
            filename=sys.argv[1]
        else:
            filename='data.csv'
        D=pd.read_csv(filename)
        
        # Calculate histograms
        y=D.Y.astype(int)
        xaks=np.linspace(D.X.min(), D.X.max(), N)
        
        h1=gaussian_kde(D[y==1].X).evaluate(xaks)
        h2=gaussian_kde(D[y==0].X).evaluate(xaks)
        #self.sliderPDF.setMinimum(D.X.min())
        #self.sliderPDF.setMaximum(D.X.max())
        #self.sliderPDF.setValue(D.X.mean())
        #self.sliderPDF.setTickInterval((D.X.max()-D.X.min())/100.0)
        #self.sliderPDF.setTickInterval(0.01)
        
        self.rocx=np.cumsum(h2)/sum(h2)
        self.rocy=np.cumsum(h1)/sum(h1)
        
        self.xdata=xaks
        self.ydata1=h1
        self.ydata2=h2


        self.replot()

    def replot(self):
        
        # create an axis
        axPDF = self.figurePDF.add_subplot(111)
        
        # discards the old graph
        axPDF.clear()
        
        # plot data
        axPDF.plot(self.xdata, self.ydata1, 'b', label='X(A=true)')
        axPDF.plot(self.xdata, self.ydata2, 'r', label='X(A=False)')

        # Decision boundary location
        dloc=self.sliderPDF.value()/100.*(max(self.xdata)-min(self.xdata))+min(self.xdata)
        axPDF.vlines(dloc, 0, max(max(self.ydata1), max(self.ydata2)), linestyles='dashed')
        axPDF.set_xlabel('X')
        axPDF.set_ylabel('Probability')
        axPDF.legend()
        axPDF.set_title('PDF of X')
        
        # refresh canvas
        self.canvasPDF.draw()

        # create an axis for ROC
        axROC = self.figureROC.add_subplot(111)
        
        # discards the old graph
        axROC.clear()
        
        if self.plotroc:
            
            # plot data
            axROC.plot(self.rocx, self.rocy, 'b')
            sensitivity=sum(self.ydata1[self.xdata<dloc])/sum(self.ydata1)
            specificity=1-sum(self.ydata2[self.xdata<dloc])/sum(self.ydata2)
            axROC.plot(1-specificity, sensitivity, 'ro')
            axROC.vlines(1-specificity, 0, 1, linestyles='dashed')
            axROC.hlines(sensitivity, 0, 1, linestyles='dashed')
            axROC.plot([0,1], [0,1], 'grey')
            axROC.set_xlabel('1-Specificity, False positive')
            axROC.set_ylabel('Sensitivity, True positive')
            axROC.set_title('ROC')
        # refresh canvas
        self.canvasROC.draw()

    def buttonClose(self):
        print("Closing")

    def ROCvaluechanged(self):
        ROCvalue = self.sliderROC.value()
        print(ROCvalue)

    def PDFvaluechanged(self):
        #PDFvalue = self.sliderPDF.value()
        #print PDFvalue
        self.replot()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())


