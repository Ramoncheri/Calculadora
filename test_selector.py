import unittest
import TkinterTestCase
import calculadora

from tkinter import *
from tkinter import ttk


class TestSelector(TkinterTestCase.TkTestCase):
    def setUp(self):
        self.s =calculadora.Selector(self.root, None)
        self.s.pack()
        self.s.wait_visibility()

    def tearDown(self):
        self.s.update()
        self.s.destroy()

    def test_render_OK(self):
        children= self.s.children
        self.assertEqual(self.s.status, 'N')
        self.assertEqual(self.s.winfo_height(), 50)
        self.assertEqual(self.s.winfo_width(), 68)
        self.assertEqual(children['btn_R'].config()['text'][4],'R')
        self.assertEqual(children['btn_N'].config()['text'][4],'N')
        self.assertTrue(isinstance(children['btn_R'], ttk.Radiobutton))
        self.assertIsInstance(children['btn_N'], ttk.Radiobutton)
        self.assertTrue(children['btn_R'].winfo_viewable(), 1)
        self.assertTrue(children['btn_N'].winfo_viewable(), 1)

    def test_init_value_R(self):
        r_selector= calculadora.Selector(self.root, None,'R')
        self.assertEqual(r_selector.status, 'R')
        r_selector.update()
        r_selector.destroy()

    def test_click_change_status(self):
        rbtn_R= self.s.children['btn_R']
        self.assertEqual(self.s.status,'N')
        self.assertEqual(self.s._Selector__value.get(), 'N')
        rbtn_R.invoke()
        self.assertEqual(self.s.status,'R')
        self.assertEqual(self.s._Selector__value.get(), 'R')

if __name__ == '__main__':
    unittest.main()