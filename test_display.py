import unittest
import TkinterTestCase
import calculadora

from tkinter import *
from tkinter import ttk


class TestDisplay(TkinterTestCase.TkTestCase):
    def setUp(self):
        self.d= calculadora.Display(self.root)
        self.d.pack()
        self.d.wait_visibility()

    def tearDown(self):
        self.d.update()
        self.d.destroy()

    def test_render_OK(self):
        self.assertEqual(self.d.winfo_height(), 50)
        self.assertEqual(self.d.winfo_width(), 272)
        self.assertEqual(self.d.value, '0')

    def test_paint_change_value(self):
        self.d.paint(20)
        self.assertEqual(self.d.value, 20)

        







#class TestSelector(unittest,TestCase):
 #   def test_render_OK(self):





if __name__ == '__main__':
    unittest.main()