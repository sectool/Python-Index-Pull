#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import urllib

index_kod_cekici_ico = """
#########################################################
#         PYTHON - INDEX PULL - GH0ST S0FTWARE          #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#        Mail Address : pentestdatabase@gmail.com       #
# LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################
"""

index_kod_cekici_mesaj = """
#########################################################
#     Site index kodu başarlı bir şekilde çekildi.      #
#########################################################
"""
star = "#########################################################"

print index_kod_cekici_ico

def index_kod_cekici():
	print star
	site_adresi = raw_input("Indexsini çekmek istediğiniz sitenin adresini giriniz : ")
	print star	
	kaynak_kod = urllib.urlopen(site_adresi).read()
	index_file = open("kaynak_kod", "w")
	index_file.write(kaynak_kod)
	index_file.close()

index_kod_cekici()
print index_kod_cekici_mesaj
