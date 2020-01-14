# -*- coding: utf-8 -*-
URL="http://demozona.staffcop.su/"
#URL_LOGIN="http://demozona.staffcop.su/accounts/login/?next=/"
L_ENG="--lang=en-us"

LANGUAGE="--lang=en-us"
#----Authorization------
#buttons and fields for authorization
el_login="id_username"
el_pass="id_password"
btn_input="//input[@value='Log in']"
#data for authorization
val_login="admin2"
val_pass="admin2"

MENU_ADMIN="//li[8]/a/i"
#"Admin"
CONTROL_PANEL="Control panel"
I_LICENSE = "License Information"
P_SETTINGS = "Server settings"
D_DIMENSION="Default GUI dimension"
VALUE_D_DIMENSION="id_value"
TEXT_DIMENSTION="(.//*[normalize-space(text()) and normalize-space(.)='Default GUI dimension'])[1]/following::td[1]"
ACCOUNTS_D_DIMENSION="Accounts"
BUTTON_D_DIMENSION="(.//*[normalize-space(text()) and normalize-space(.)='Value:'])[1]/following::option[3]"
BTN_SAVE_DIMENSION="_return"
BTN_HOME="//i"
MENU_TIME_TRACKING="Time tracking"
#XPATH_TIME_TRACKING="(.//*[normalize-space(text()) and normalize-space(.)='Statistics'])[2]/following::span[1]"
COMBINED_REPORT="Combined report"
NAME_PAGE="//body"