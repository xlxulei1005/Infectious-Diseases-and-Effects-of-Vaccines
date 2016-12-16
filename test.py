import unittest
from object_class import *
from exception_class import *


class Test(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_color_class(self):
        self.assertEqual(color_class('0.8').color,0.8)
        
        with self.assertRaises(colorrangeException):
            color_class('8')
        with self.assertRaises(colorrangeException):
            color_class('-1')
        with self.assertRaises(colortypeException):
            color_class('dsfdfe')

        
    def test_year_class(self):
        self.assertEqual(year_class('1978','MUMPS').year,1978)
        
        with self.assertRaises(yeartypeException):
            year_class('19fewwv','MUMPS')
        with self.assertRaises(yearrangeException):
            year_class('1900','MEASLES')
        with self.assertRaises(yearrangeException):
            year_class('1960','SMALLPOX')
               
    def test_disease_class(self):
        self.assertEqual(disease_class('MUMPS').name,'MUMPS')
        self.assertEqual(disease_class('MUMPS').lower,1968)
        self.assertEqual(disease_class('MUMPS').upper,2014)
        
        with self.assertRaises(diseaseExceptioin):
            disease_class('vfdvfdv')
                     

if __name__ =='__main__':
    unittest.main()