#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Apr 30 14:37:27 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import numbersink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.freq_0 = freq_0 = 525.2e6
        self.threshold = threshold = -60
        self.samp_rate = samp_rate = 2.048e6
        self.freq = freq = freq_0

        ##################################################
        # Blocks
        ##################################################
        _threshold_sizer = wx.BoxSizer(wx.VERTICAL)
        self._threshold_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_threshold_sizer,
        	value=self.threshold,
        	callback=self.set_threshold,
        	label="threshold",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._threshold_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_threshold_sizer,
        	value=self.threshold,
        	callback=self.set_threshold,
        	minimum=-100,
        	maximum=0,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_threshold_sizer)
        self.wxgui_numbersink2_0_0 = numbersink2.number_sink_f(
        	self.GetWin(),
        	unit="signal present",
        	minval=0,
        	maxval=1,
        	factor=1.0,
        	decimal_places=10,
        	ref_level=0,
        	sample_rate=2.048e6,
        	number_rate=15,
        	average=False,
        	avg_alpha=None,
        	label="Signal detection",
        	peak_hold=False,
        	show_gauge=True,
        )
        self.Add(self.wxgui_numbersink2_0_0.win)
        self.wxgui_numbersink2_0 = numbersink2.number_sink_f(
        	self.GetWin(),
        	unit="Units",
        	minval=-120,
        	maxval=0,
        	factor=1.0,
        	decimal_places=10,
        	ref_level=0,
        	sample_rate=2048000,
        	number_rate=15,
        	average=True,
        	avg_alpha=0.03,
        	label="Level",
        	peak_hold=False,
        	show_gauge=True,
        )
        self.Add(self.wxgui_numbersink2_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=2048000,
        	fft_size=1024,
        	fft_rate=15,
        	average=True,
        	avg_alpha=0.030,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(2.048e6)
        self.rtlsdr_source_0.set_center_freq(freq, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(2, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(10, 0)
        self.rtlsdr_source_0.set_if_gain(10, 0)
        self.rtlsdr_source_0.set_bb_gain(5, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab1")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab2")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab3")
        self.Add(self.notebook_0)
        _freq_0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_0_sizer,
        	value=self.freq_0,
        	callback=self.set_freq_0,
        	label='freq_0',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_0_sizer,
        	value=self.freq_0,
        	callback=self.set_freq_0,
        	minimum=478e6,
        	maximum=862e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_0_sizer)
        self.fft_vxx_0 = fft.fft_vcc(1024, True, (window.rectangular(1024)), True, 1)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, 2048000,True)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(-100, threshold, -60)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 1024)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_int*1, "/media/ubuntu/01D165566F075780/Q3/wireless networking/GNU/out1.txt", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_divide_xx_0 = blocks.divide_ff(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1024)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1.04858e6)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_divide_xx_0, 1))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_vector_to_stream_0, 0))    
        self.connect((self.blocks_divide_xx_0, 0), (self.blocks_nlog10_ff_0, 0))    
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_threshold_ff_0, 0))    
        self.connect((self.blocks_nlog10_ff_0, 0), (self.wxgui_numbersink2_0, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))    
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blocks_threshold_ff_0, 0), (self.wxgui_numbersink2_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_vector_0, 0))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_divide_xx_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.wxgui_fftsink2_0, 0))    


    def get_freq_0(self):
        return self.freq_0

    def set_freq_0(self, freq_0):
        self.freq_0 = freq_0
        self.set_freq(self.freq_0)
        self._freq_0_slider.set_value(self.freq_0)
        self._freq_0_text_box.set_value(self.freq_0)

    def get_threshold(self):
        return self.threshold

    def set_threshold(self, threshold):
        self.threshold = threshold
        self._threshold_slider.set_value(self.threshold)
        self._threshold_text_box.set_value(self.threshold)
        self.blocks_threshold_ff_0.set_hi(self.threshold)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.rtlsdr_source_0.set_center_freq(self.freq, 0)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Start(True)
    tb.Wait()
