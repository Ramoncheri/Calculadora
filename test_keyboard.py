import unittest
import TkinterTestCase
import calculadora
from tkinter import *
from tkinter import ttk

class testKeyboard(TkinterTestCase.TkTestCase):
    def setUp(self):
        self.k= calculadora.Keyboard(self.root)
        self.k.pack()
        self.k.wait_visibility()

    def tearDown(self):
        self.k.update()
        self.k.destroy()

    def test_render_OK(self):
        self.assertEqual(self.k.winfo_height(), 250)
        self.assertEqual(self.k.winfo_width(), 272)
        for btn in self.k.children.values():
            self.assertIsInstance(btn, calculadora.CalcButton)
        self.assertEqual(len(self.k.listaBNormales), 18)
        self.assertEqual(len(self.k.listaBRomanos), 0)


    def test_render_romano_OK(self):
        teclado_romano= calculadora.Keyboard(self.root, 'R')
        teclado_romano.pack()
        teclado_romano.wait_visibility()
        self.assertEqual(teclado_romano.winfo_height(), 250)
        self.assertEqual(teclado_romano.winfo_width(), 272)
        for btn in teclado_romano.children.values():
            self.assertIsInstance(btn, calculadora.CalcButton)
        self.assertEqual(len(teclado_romano.children), 13)
        self.assertEqual(len(teclado_romano.listaBNormales), 0)
        self.assertEqual(len(teclado_romano.listaBRomanos), 13)
       
        teclado_romano.update()
        teclado_romano.destroy()

    def test_change_status_keyboard(self):
        self.assertEqual(self.k.status, 'N')
        self.k.status= 'R'
        for btn in self.k.children.values():
            self.assertIsInstance(btn, calculadora.CalcButton)
        self.assertEqual(len(self.k.children), 31)
        self.assertEqual(self.k.status, 'R')
        self.assertEqual(len(self.k.listaBNormales), 18)
        self.assertEqual(len(self.k.listaBRomanos), 13)



if __name__ == '__main__':
    unittest.main()