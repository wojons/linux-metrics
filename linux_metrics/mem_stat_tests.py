#!/usr/bin/env python
#
#  Copyright (c) 2010-2012 Corey Goldberg (http://goldb.org)
#
#  This file is part of linux-metrics
#
#  License :: OSI Approved :: MIT License:
#      http://www.opensource.org/licenses/mit-license
# 
#      Permission is hereby granted, free of charge, to any person obtaining a copy
#      of this software and associated documentation files (the "Software"), to deal
#      in the Software without restriction, including without limitation the rights
#      to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#      copies of the Software, and to permit persons to whom the Software is
#      furnished to do so, subject to the following conditions:
#
#      The above copyright notice and this permission notice shall be included in
#      all copies or substantial portions of the Software.
#


import mem_stat
import unittest



class TestMemoryStats(unittest.TestCase):
    
    def test_mem_used(self):
        value, _ = mem_stat.mem_stats()
        self.assertTrue(value > 0, value)
        
    def test_mem_total(self):
        _, value = mem_stat.mem_stats()
        self.assertTrue(value > 0, value)
            


if __name__ == '__main__':  
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestMemoryStats)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
