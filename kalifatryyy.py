# ----------StartImport module--------------
import time
from tkinter import *
from tkinter import messagebox
from turtle import width
from PIL import Image,ImageTk
from tkinter import ttk
import socket
import itertools
import requests

# ------------End Import module--------------
#PACKET PRIMARY HEADER
adcs_para = []
def adcs_para_conv():
    #global my
    for i in itertools.product([0,1],repeat=8):
        s= ''.join(str(v) for v in i)
        adcs_para.append(s)
adcs_para_conv()
bit_count = 0 #PACKET SEQUENCE COUNT OR PACKET NAME
packet_version_number = '000'
packet_type = '0'
sec_hdr_flag = '0'
seq_flag = '00' #SEQUENCE FLAG
packet_data_len = '1' #PACKET DATA LENGTH
packet_data_len2 = '3' #PACKET DATA LENGTH
command_counter=0
commandonlist=''
#---------------------------------------------------#

Temp_OBC='00000011010'
Volt_OBC='00000001010'
Current_OBC='00000010010'

Temp_Power='00000011001'
Volt_Power='00000001001'
Current_Power='00000010001'


Temp_Comm='00000011011'
Volt_Comm='00000001011'
Current_Comm='00000010011'

Temp_Cam='00000011100'
Volt_Cam='00000001100'
Current_Cam='00000010100'

Temp_ADCS='00000011000'
Volt_ADCS='00000001000'
Current_ADCS='00000010000'



#---------------------------------------------------#
#SUBSYSTEM CODE
OBC_id = '00000000010'
power_id = '00000000001'
comm_id = '00000000011'
cam_id = '00000000100'
ADCS_id = '00000000000'
#PROCESS CODE OBC
on_OBC = '00000000'
off_OBC = '00000001'
OBC_telem = '00000011'
#PROCESS CODE CAM
on_Cam = '00000110'
off_Cam = '00000111'
take_Cam = '00001000'
send_Cam = '00001001'
Cam_telem = '00001010'
#PROCESS CODE POWER
on_Power = '00001101'
off_Power = '00001110'
Power_telem = '00001111'
#PROCESS CODE COMMUNICATION
on_Comm = '00010010'
off_Comm = '00010011'
Comm_telem = '00010100'

#PROCESS CODE ADCS
on_ADCS = '00010111'
off_ADCS = '00011000'
ADCS_telem = '00011001'
ADCS_parametr_x_y = '00011010' #then the byte of x then the byte of y
#ADCS_parametr_y = '00000010'

direct_temp ='11000000'
direct_volt = '01000000'
direct_current = '10000000'
my = []
def Bit_Count_Fun():
    for i in itertools.product([0,1],repeat=14):
        s= ''.join(str(v) for v in i)
        my.append(s)
Bit_Count_Fun()
# ------------ needed variables -------------
obc_on=0;
obc_off=0;
obc_temp_telem=0;
obc_volt_telem=0;
obc_curr_telem=0;
#----------------
power_on=0;
power_off=0;
power_temp_telem=0;
power_volt_telem=0;
power_curr_telem=0;
#-------------------
comm_on=0;
comm_off=0;
comm_temp_telem=0;
comm_volt_telem=0;
comm_curr_telem=0;
#-------------------
cam_on=0;
cam_off=0;
cam_temp_telem=0;
cam_volt_telem=0;
cam_curr_telem=0;
cam_take_photo=0;
cam_send_photo=0;
#-------------------
adcs_on=0;
adcs_off=0;
adcs_temp_telem=0;
adcs_volt_telem=0;
adcs_curr_telem=0;
adcs_send_parameter=0;
x_parameter=''
y_parameter=''
#--------------------------------------------
##second_window=''
##third_window=''
conn =''
# ------------Functions module--------------
second_window=Tk
# ------------------------------------------- Start session function --------------------------------------------------------------------------------------
def showImg():
    sended_image_var = Toplevel(second_window)
    sended_image_var.title("Taked Photo")
    sended_image_var.geometry("700x500")
    load = Image.open('bb.png')
    render = ImageTk.PhotoImage(load)
    img = Label(sended_image_var, image=render)
    img.image = render
    img.place(x=0, y=0)

def rr():
    with open('Telemetry.txt', 'a') as tl:
        tl.write(Result+'\n')

def textinsert():
    TLM.insert(INSERT, Result+'\n')

def progressinsert(msg):
    Progress.insert(INSERT,msg+'\n')

def start_session():
    global command_counter
    with open('commandcounter.txt','w') as jo:
        jo.write(str(command_counter))
    while command_counter>0:
        command_counter-=1
        #i declare coon here but it's not here erase it when you but the two codes togither
        global obc_on
        global obc_off
        global obc_temp_telem
        global obc_volt_telem
        global obc_curr_telem
        global power_on
        global power_off
        global power_temp_telem
        global power_volt_telem
        global power_curr_telem
        global comm_on
        global comm_off
        global comm_temp_telem
        global comm_volt_telem
        global comm_curr_telem
        global cam_on
        global cam_off
        global cam_temp_telem
        global cam_volt_telem
        global cam_curr_telem
        global cam_take_photo
        global cam_send_photo
        global adcs_on
        global adcs_off
        global adcs_temp_telem
        global adcs_volt_telem
        global adcs_curr_telem
        global adcs_send_parameter
        global conn
        global my
        global bit_count
        global Result
        global msg
        bit_count += 1
        if obc_on == 1:
            msg='Sending The \'OBC ON\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + OBC_id + seq_flag + my[bit_count] + packet_data_len + on_OBC).encode())
            msg='Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg='Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg='Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg='Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            textinsert()
            obc_on = 0
        elif obc_off ==1:
            msg = 'Sending The \'OFF OBC\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + OBC_id + seq_flag + my[bit_count] + packet_data_len + off_OBC).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            textinsert()
            obc_off =0
        elif obc_temp_telem == 1:
            msg = 'Sending The \'OBC LDR Telemetry\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + Temp_OBC + seq_flag + my[bit_count] + packet_data_len + OBC_telem).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            rr()
            textinsert()
            obc_temp_telem =0
        elif obc_volt_telem == 1:
            msg = 'Sending The \'OBC VOLTAGE TELEMETRY\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + Volt_OBC + seq_flag + my[bit_count] + packet_data_len + OBC_telem).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            rr()
            textinsert()
            obc_volt_telem =0
        elif obc_curr_telem == 1:
            msg = 'Sending The \'OBC GYRO TELEMETRY\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + Current_OBC + seq_flag + my[bit_count] + packet_data_len + OBC_telem).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            rr()
            textinsert()
            obc_curr_telem = 0
        elif power_on == 1:
            msg = 'Sending The \'Power ON\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + power_id + seq_flag + my[bit_count] + packet_data_len + on_Power).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            textinsert()
            power_on = 0
        elif power_off == 1:
            msg = 'Sending The \'Power OFF\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + power_id + seq_flag + my[bit_count] + packet_data_len + off_Power).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            textinsert()
            power_off =0
        elif power_temp_telem == 1:
            msg = 'Sending The \'Power LDR TELEMETRY\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + Temp_Power + seq_flag + my[bit_count] + packet_data_len + Power_telem).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            rr()
            textinsert()
            power_temp_telem =0
        elif power_volt_telem == 1:
            msg = 'Sending The \'Power VOLTAGE TELEMETRY\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + Volt_Power + seq_flag + my[bit_count] + packet_data_len + Power_telem).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            rr()
            textinsert()
            power_volt_telem =0
        elif power_curr_telem == 1:
            msg = 'Sending The \'Power GYRO TELEMETRY\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + Current_Power + seq_flag + my[bit_count] + packet_data_len + Power_telem).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            rr()
            textinsert()
            power_curr_telem =0
        elif comm_on == 1:
            msg = 'Sending The \'Communication ON\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + comm_id + seq_flag + my[bit_count] + packet_data_len + on_Comm).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            textinsert()
            comm_on =0
        elif comm_off == 1:
            msg = 'Sending The \'Communication OFF\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + comm_id + seq_flag + my[bit_count] + packet_data_len + off_Comm).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            textinsert()
            comm_off =0
        elif comm_temp_telem == 1:
            msg = 'Sending The \'Communication LDR TELEMETRY\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + Temp_Comm + seq_flag + my[bit_count] + packet_data_len + Comm_telem).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            rr()
            textinsert()
            comm_temp_telem =0
        elif comm_volt_telem == 1:
            msg = 'Sending The \'Communication VOLTAGE TELEMETRY\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + Volt_Comm + seq_flag + my[bit_count] + packet_data_len + Comm_telem).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            rr()
            textinsert()
            comm_volt_telem =0
        elif comm_curr_telem == 1:
            msg = 'Sending The \'Communication GYRO TELEMETRY\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + Current_Comm + seq_flag + my[bit_count] + packet_data_len + Comm_telem).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            rr()
            textinsert()
            comm_curr_telem =0
        elif cam_on == 1:
            msg = 'Sending The \'Camera ON\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + cam_id + seq_flag + my[bit_count] + packet_data_len + on_Cam).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            textinsert()
            cam_on =0
        elif cam_off == 1:
            msg = 'Sending The \'Camera OFF\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + cam_id + seq_flag + my[bit_count] + packet_data_len + off_Cam).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            textinsert()
            cam_off =0
        elif cam_temp_telem == 1:
            msg = 'Sending The \'Camera LDR TELEMETRY\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + Temp_Cam + seq_flag + my[bit_count] + packet_data_len + Cam_telem).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            rr()
            textinsert()
            cam_temp_telem =0
        elif cam_volt_telem == 1:
            msg = 'Sending The \'Camera VOLTAGE TELEMETRY\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + Volt_Cam + seq_flag + my[bit_count] + packet_data_len + Cam_telem).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            rr()
            textinsert()
            cam_volt_telem =0
        elif cam_curr_telem == 1:
            msg = 'Sending The \'Camera GYRO TELEMETRY\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + Current_Cam + seq_flag + my[bit_count] + packet_data_len + Cam_telem).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            rr()
            textinsert()
            cam_curr_telem =0
        elif cam_take_photo == 1:
            msg = 'Sending The \'Camera Take Photo\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + cam_id + seq_flag + my[bit_count] + packet_data_len + take_Cam).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            textinsert()
            cam_take_photo =0
        elif cam_send_photo == 1:
            msg = 'Sending The \'Camera Receive Photo\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + ADCS_id + seq_flag + my[bit_count] + packet_data_len + send_Cam).encode())
            #Acknowledge = conn.recv(1024).decode()
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode
            msg = 'Received Image From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Image....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Image Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            r = requests.get('http://192.168.1.5:2560/')
            comm = r.content
            with open('TheSatelliteReceivedPhoto.jpg', 'wb') as oir:
                oir.write(comm)
            global immg
            immg = ImageTk.PhotoImage(Image.open("TheSatelliteReceivedPhoto.jpg"))
            #with Image.open('TheSatelliteRecivedPhoto.jpg') as img:
             #   img.show()
            #with open('SatelliteNewPhoto.jpg', 'wb') as wb:
                #wb.write(Result)
            #with Image.open('SatelliteNewPhoto.jpg') as img:
                #img.show()
            #textinsert()
            cam_send_photo =0
        elif adcs_on == 1:
            msg = 'Sending The \'ADCS ON\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + ADCS_id + seq_flag + my[bit_count] + packet_data_len + on_ADCS).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            textinsert()
            adcs_on =0
        elif adcs_off == 1:
            msg = 'Sending The \'ADCS OFF\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + ADCS_id + seq_flag + my[bit_count] + packet_data_len + off_ADCS).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            textinsert()
            adcs_off =0
        elif adcs_temp_telem == 1:
            msg = 'Sending The \'ADCS LDR TELEMETRY\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + Temp_ADCS + seq_flag + my[bit_count] + packet_data_len + ADCS_telem).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            rr()
            textinsert()
            adcs_temp_telem =0
        elif adcs_volt_telem == 1:
            msg = 'Sending The \'ADCS VOLTAGE TELEMETRY\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + Volt_ADCS + seq_flag + my[bit_count] + packet_data_len + ADCS_telem).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            rr()
            textinsert()
            adcs_volt_telem =0
        elif adcs_curr_telem == 1:
            msg = 'Sending The \'ADCS GYRO TELEMETRY\' Command...'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            conn.send((packet_version_number + packet_type + sec_hdr_flag + Current_ADCS + seq_flag + my[bit_count] + packet_data_len + ADCS_telem).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            rr()
            textinsert()
            adcs_curr_telem =0
        elif adcs_send_parameter ==1:
            msg = 'Sending The \'Angels\' Commands (Yaw & Pitch) Angels....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            x_para=x_parameter.get()
            y_para=y_parameter.get()
            print(x_para)
            p = int(x_para)
            print(type(p))
            p=str(adcs_para[p])
            print(type(p))
            c = int(y_para)
            c = str(adcs_para[c])
            conn.send((packet_version_number + packet_type + sec_hdr_flag + ADCS_id + seq_flag + my[bit_count] + packet_data_len + ADCS_parametr_x_y + p + c).encode())
            msg = 'Command Sent Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Waiting For Data From Satellite... '
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            Result = conn.recv(1073741824).decode()
            msg = 'Received Data From The Satellite Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Saving Data....'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            msg = 'Data Saved Successfully ✔'
            progressinsert(msg)
            first_window.update()
            time.sleep(2)
            textinsert()
            adcs_send_parameter =0
# ------------------------------------------------------------------------- start session function done!! ----------------------------------------------------------------------------------------
def obc1_on():
    global command_counter
    command_counter+=1
    global commandonlist
    commandonlist='On OBC'
    #print("obc1_on entered")
    global obc_on
    obc_on = 1
    #print(obc_on)
def obc1_off():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'OFF OBC'
    global obc_off
    obc_off = 1
def obc1_temp():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'OBC LDR Telemetry'
    global obc_temp_telem
    obc_temp_telem = 1
def obc1_volt():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'OBC Voltage Telemetry'
    global obc_volt_telem
    obc_volt_telem = 1
def obc1_curr():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'OBC Gyro Telemetry'
    global obc_curr_telem
    obc_curr_telem = 1
def power1_on():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'On Power'
    global power_on
    power_on = 1
def power1_off():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'OFF Power'
    global power_off
    power_off = 1
def power1_temp():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'Power LDR Telemetry'
    global power_temp_telem
    power_temp_telem = 1
def power1_volt():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'Power Voltage Telemetry'
    global power_volt_telem
    power_volt_telem = 1
def power1_curr():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'Power Gyro Telemetry'
    global power_curr_telem
    power_curr_telem =1
def comm1_on():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'On Communication'
    global comm_on
    comm_on = 1
def comm1_off():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'OFF Communication'
    global comm_off
    comm_off = 1
def comm1_temp():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'Communication LDR Telemetry'
    global comm_temp_telem
    comm_temp_telem = 1
def comm1_volt():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'Communication Voltage Telemetry'
    global comm_volt_telem
    comm_volt_telem = 1
def comm1_curr():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'Communication Gyro Telemetry'
    global comm_curr_telem
    comm_curr_telem =1
def cam1_on():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'On Camera'
    global cam_on
    cam_on = 1
def cam1_off():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'OFF Camera'
    global cam_off
    cam_off = 1
def cam1_temp():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'Camera LDR Telemetry'
    global cam_temp_telem
    cam_temp_telem = 1
def cam1_volt():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'Camera Voltage Telemetry'
    global cam_volt_telem
    cam_volt_telem = 1
def cam1_curr():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'Camera Gyro Telemetry'
    global cam_curr_telem
    cam_curr_telem =1
def cam1_take():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'Take Photo'
    global cam_take_photo
    cam_take_photo = 1
def cam1_send():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'Receive Photo'
    global cam_send_photo
    cam_send_photo =1
    #showImg()
def adcs1_on():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'On ADCS'
    global adcs_on
    adcs_on = 1
def adcs1_off():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'OFF ADCS'
    global adcs_off
    adcs_off = 1
def adcs1_temp():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'ADCS LDR Telemetry'
    global adcs_temp_telem
    adcs_temp_telem = 1
def adcs1_volt():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'Camera Voltage Telemetry'
    global adcs_volt_telem
    adcs_volt_telem = 1
def adcs1_curr():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'Camera Gyro Telemetry'
    global adcs_curr_telem
    adcs_curr_telem =1
def adcs1_take():
    global command_counter
    command_counter += 1
    global commandonlist
    commandonlist = 'ADCS Angels'
    global adcs_send_parameter
    adcs_send_parameter = 1
#-----------------------------------------------------------------------------------------------------
def open_new_window():
    opensecond_window()
def delay():
    first_window.after(2000, open_new_window)
# -----------End functions module-----------
ope=''
# -----------------Start Program module-------------------
first_window = Tk()
first_window.title("Swarm System Project")
first_window.state('zoomed')
first_window.config(bg='#C0C0C0')
#first_window.eval('tk::PlaceWindow . center')
# Adjust size

first_window.geometry("700x500")
'''
def server_program():
# -----------Start the New window module------------------
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024
    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind(('', port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from Swarm Satellite is Established At : " + str(address))
    Beacon = conn.recv(1024).decode()
    print('Recevied Beacon From Swarm Satellite : ' + Beacon)
'''
def openthird_window():
    global third_window
    global third_img
    global Lb2
    third_window = Toplevel()
    third_window.title("Progress")
    third_window.geometry("700x500")
    Lb2 = Listbox(third_window, border=2, width=30)
    Lb2.pack(side=LEFT, fill=BOTH)
    scrollbar = Scrollbar(third_window)
    scrollbar.pack(side=RIGHT, fill=BOTH)
    Lb2.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=Lb2.yview)
    #third_window = PhotoImage(file="second pic.png")
    #label = Label(third_window, image=Second_img)
    #label.place(x=0, y=0)

def operator():
    global ope
    ope='go'
    print('in fun')
    print(ope)

def opensecond_window():
    global Second_img
    global second_window
    second_window = Toplevel()
    second_window.title("Swarm Subsystems & Process")
    second_window.geometry("700x500")
    Second_img = PhotoImage(file="space_11.png")
    label = Label(second_window, image=Second_img)
    label.place(x=0, y=0)
    ttk.Label(first_window, text="Select Subsystem Then Press Enter", background='black', foreground="white",
              font=("Times New Roman", 13)).place(x=230,y=7)



    def mass_box(x,y):
        messagebox.showinfo(x,y,parent=first_window)

    # datatype of menu text
    clicked = StringVar()
    # initial menu text
    clicked.set("OBC")
    # Create Dropdown menu
    drop = ttk.Combobox(first_window, width=27, textvariable=clicked)
    drop['values'] = (    'OBC',
                          'POWER',
                          'COMMUNICATION',
                          'CAMERA',
                          'ADCS',
    )

    def show():
        clicked
        if clicked.get() == "ADCS":
            ADCS_menu()
        elif clicked.get() == "OBC":
            OBC_menu()
        elif clicked.get() == "CAMERA":
            Camera_menu()
        elif clicked.get() == "POWER":
            Power_menu()
        elif clicked.get() == "COMMUNICATION":
            Communication_menu()


    def OBC_menu():
        # All Buttons Needs Commends
        On_button = Button(first_window, bg='#e91e63' ,fg='white',borderwidth=3  , text="ON OBC",font=("Times New Roman",10),width =25,height = 2,command=lambda: [obc1_on(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        On_button.place(x = 10,y = 200)
        OFF_button = Button(first_window, bg='#e91e63' ,fg='white',borderwidth=3  ,text="OFF OBC",font=("Times New Roman",10),width =25,height = 2,command=lambda: [obc1_off(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        OFF_button.place(x = 280,y = 200)
        back_button = Button(first_window, bg='#000000' ,fg='white',borderwidth=3  ,text="Back",font=("Times New Roman",10),width =25,height = 2, command=lambda: [On_button.destroy(), OFF_button.destroy(),
                                                                 Temp_Telemetry_button.destroy(),
                                                                 Volt_Telemetry_button.destroy(),
                                                                 Current_Telemetry_button.destroy(),
                                                                 back_button.destroy()])
        back_button.place(x = 500,y = 200)
        Temp_Telemetry_button = Button(first_window,bg='#e91e63' ,fg='white',borderwidth=3  , text="OBC LDR Telemetry",font=("Times New Roman",10),width =25,height = 2,command=lambda: [obc1_temp(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        Temp_Telemetry_button.place(x = 10,y = 300)
        Volt_Telemetry_button = Button(first_window,bg='#e91e63' ,fg='white',borderwidth=3  , text="OBC Voltage Telemetry",font=("Times New Roman",10),width =25,height = 2,command=lambda: [obc1_volt(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        Volt_Telemetry_button.place(x = 280,y = 300)
        Current_Telemetry_button = Button(first_window, bg='#e91e63' ,fg='white',borderwidth=3  ,text="OBC Gyro Telemetry",font=("Times New Roman",10),width =25,height = 2,command=lambda: [obc1_curr(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        Current_Telemetry_button.place(x = 500,y = 300)

    def Power_menu():
        # All Buttons Needs Commends
        On_button = Button(first_window,bg='#1A237E' ,fg='white',borderwidth=3  , text="ON Power",font=("Times New Roman",10),width =25,height = 2,command=lambda: [power1_on(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        On_button.place(x = 10,y = 200)
        OFF_button = Button(first_window, bg='#1A237E' ,fg='white',borderwidth=3  ,text="OFF Power",font=("Times New Roman",10),width =25,height = 2,command=lambda: [power1_off(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        OFF_button.place(x = 280,y = 200)
        Temp_Telemetry_button = Button(first_window, bg='#1A237E' ,fg='white',borderwidth=3  ,text="Power LDR Telemetry",font=("Times New Roman",10),width =25,height = 2,command=lambda: [power1_temp(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        Temp_Telemetry_button.place(x = 10,y = 300)
        Volt_Telemetry_button = Button(first_window, bg='#1A237E' ,fg='white',borderwidth=3  ,text="Power Voltage Telemetry",font=("Times New Roman",10),width =25,height = 2,command=lambda: [power1_volt(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        Volt_Telemetry_button.place(x = 280,y = 300)
        Current_Telemetry_button = Button(first_window,bg='#1A237E' ,fg='white',borderwidth=3  , text="Power Gyro Telemetry",font=("Times New Roman",10),width =25,height = 2,command=lambda: [power1_curr(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        Current_Telemetry_button.place(x = 500,y = 300)
        back_button = Button(first_window, bg='#000000' ,fg='white',borderwidth=3  ,text="Back",font=("Times New Roman",10),width =25,height = 2, command=lambda: [On_button.destroy(), OFF_button.destroy(),
                                                                 Temp_Telemetry_button.destroy(),
                                                                 Volt_Telemetry_button.destroy(),
                                                                 Current_Telemetry_button.destroy(),
                                                                 back_button.destroy()])
        back_button.place(x = 500,y = 200)



    def Communication_menu():
        # All Buttons Needs Commends
        On_button = Button(first_window,bg='#B2EBF2' ,fg='black',borderwidth=3  , text="ON Communication",font=("Times New Roman",10),width =30,height = 2,command=lambda: [comm1_on(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        On_button.place(x = 10,y = 200)
        OFF_button = Button(first_window,bg='#B2EBF2' ,fg='black',borderwidth=3  , text="OFF Communication",font=("Times New Roman",10),width =27,height = 2,command=lambda: [comm1_off(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        OFF_button.place(x = 255,y = 200)
        Temp_Telemetry_button = Button(first_window,bg='#B2EBF2' ,fg='black',borderwidth=3  , text="Communication LDR Telemetry",font=("Times New Roman",10),width =30,height = 2,command=lambda: [comm1_temp(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        Temp_Telemetry_button.place(x = 10,y = 300)
        Volt_Telemetry_button = Button(first_window,bg='#B2EBF2' ,fg='black',borderwidth=3  , text="Communication Voltage Telemetry",font=("Times New Roman",10),width =27,height = 2,command=lambda: [comm1_volt(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        Volt_Telemetry_button.place(x = 255,y = 300)
        Current_Telemetry_button = Button(first_window,bg='#B2EBF2' ,fg='black',borderwidth=3  , text="Communication Gyro Telemetry",font=("Times New Roman",10),width =28,height = 2,command=lambda: [comm1_curr(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        Current_Telemetry_button.place(x = 480,y = 300)
        back_button = Button(first_window, bg='#000000' ,fg='white',borderwidth=3  ,text="Back",font=("Times New Roman",10),width =28,height = 2, command=lambda: [On_button.destroy(), OFF_button.destroy(),
                                                                 Temp_Telemetry_button.destroy(),
                                                                 Volt_Telemetry_button.destroy(),
                                                                 Current_Telemetry_button.destroy(),
                                                                 back_button.destroy()])
        back_button.place(x = 480,y = 200)

    def Camera_menu():
        # All Buttons Needs Commends
        On_button = Button(first_window, bg='#FB8C00' ,fg='black',borderwidth=3  , text="ON Camera",font=("Times New Roman",10),width =25,height = 2,command=lambda: [cam1_on(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        On_button.place(x = 10,y = 200)
        OFF_button = Button(first_window,bg='#FB8C00' ,fg='black',borderwidth=3  , text="OFF Camera",font=("Times New Roman",10),width =25,height = 2,command=lambda: [cam1_off(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        OFF_button.place(x = 255,y = 200)
        Temp_Telemetry_button = Button(first_window, bg='#FB8C00' ,fg='black',borderwidth=3  ,text="Camera LDR Telemetry",font=("Times New Roman",10),width =25,height = 2,command=lambda: [cam1_temp(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        Temp_Telemetry_button.place(x = 10,y = 300)
        Volt_Telemetry_button = Button(first_window, bg='#FB8C00' ,fg='black',borderwidth=3  ,text="Camera Voltage Telemetry",font=("Times New Roman",10),width =25,height = 2,command=lambda: [cam1_volt(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        Volt_Telemetry_button.place(x = 255,y = 300)
        Current_Telemetry_button = Button(first_window, bg='#FB8C00' ,fg='black',borderwidth=3  ,text="Camera Gyro Telemetry",font=("Times New Roman",10),width =25,height = 2,command=lambda: [cam1_curr(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        Current_Telemetry_button.place(x = 480,y = 300)
        Take_button = Button(first_window,bg='#FB8C00' ,fg='black',borderwidth=3  , text="Take Photo",font=("Times New Roman",10),width =25,height = 2,command=lambda: [cam1_take(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        Take_button.place(x = 480,y = 200)
        Send_button = Button(first_window,bg='#FB8C00' ,fg='black',borderwidth=3  , text="Receive Photo",font=("Times New Roman",10),width =25,height = 2,command=lambda: [cam1_send(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        Send_button.place(x=110,y=400)
        back_button = Button(first_window,bg='#000000' ,fg='white',borderwidth=3  , text="Back",font=("Times New Roman",10),width =25,height = 2, command=lambda: [On_button.destroy(), OFF_button.destroy(),
                                                                 Temp_Telemetry_button.destroy(),
                                                                 Volt_Telemetry_button.destroy(),
                                                                 Current_Telemetry_button.destroy(),
                                                                 Send_button.destroy(), Take_button.destroy(),
                                                                 back_button.destroy()])
        back_button.place(x = 350,y = 400)


    def ADCS_menu():
        # All Buttons Needs Commends
        global x_parameter
        global y_parameter
        global y_parameter_input
        global x_parameter_input
        On_button = Button(first_window, bg='#43A047' ,fg='black',borderwidth=3  ,text="ON ADCS",font=("Times New Roman",10),width =25,height = 2,command=lambda: [adcs1_on(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        On_button.place(x = 10,y = 200)
        OFF_button = Button(first_window,bg='#43A047' ,fg='black',borderwidth=3  , text="OFF ADCS",font=("Times New Roman",10),width =25,height = 2,command=lambda: [adcs1_off(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        OFF_button.place(x = 255,y = 200)
        Temp_Telemetry_button = Button(first_window, bg='#43A047' ,fg='black',borderwidth=3  ,text="ADCS LDR Telemetry",font=("Times New Roman",10),width =25,height = 2,command=lambda: [adcs1_temp(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        Temp_Telemetry_button.place(x = 10,y = 300)
        Volt_Telemetry_button = Button(first_window,bg='#43A047' ,fg='black',borderwidth=3  , text="ADCS Voltage Telemetry",font=("Times New Roman",10),width =25,height = 2,command=lambda: [adcs1_volt(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        Volt_Telemetry_button.place(x = 255,y = 300)
        Current_Telemetry_button = Button(first_window,bg='#43A047' ,fg='black',borderwidth=3  , text="ADCS Gyro Telemetry",font=("Times New Roman",10),width =25,height = 2,command=lambda: [adcs1_curr(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        Current_Telemetry_button.place(x = 480,y = 300)
        label_x = Label(first_window,bg='#43A047' ,fg='black',borderwidth=3  , text="Enter Yaw Angel",font=("Times New Roman",10),width =25)
        label_x.place(x = 155,y = 360)
        x_parameter = StringVar()
        x_parameter.set("90")
        x_parameter_input = Entry(first_window, width=3, textvariable=x_parameter)
        x_parameter_input.place(x = 235,y = 400)
        label_y = Label(first_window, bg='#43A047' ,fg='black',borderwidth=3  ,text="Enter Pitch Angel",font=("Times New Roman",10),width =25)
        label_y.place(x = 350,y = 360)
        y_parameter = StringVar()
        y_parameter.set("90")
        y_parameter_input = Entry(first_window, width=3, textvariable=y_parameter)
        y_parameter_input.place(x = 415,y = 400)
        Enter_button = Button(first_window,bg='#43A047' ,fg='black',borderwidth=3  , text="Send Angels",font=("Times New Roman",10),width =20,height = 1,command=lambda: [adcs1_take(),Lb1.insert(command_counter, f'{command_counter}-{commandonlist}')])
        Enter_button.place(x=260,y=430)
        back_button = Button(first_window, bg='#000000' ,fg='white',borderwidth=3  ,text="Back",font=("Times New Roman",10),width =25,height =2,
                             command=lambda: [On_button.destroy(), OFF_button.destroy(), x_parameter_input.destroy(),
                                              y_parameter_input.destroy(), Temp_Telemetry_button.destroy(),
                                              Volt_Telemetry_button.destroy(), Current_Telemetry_button.destroy(),
                                              label_y.destroy(), label_x.destroy(), Enter_button.destroy(),
                                              back_button.destroy()])
        back_button.place(x = 480,y = 200)


    drop.place(x=270,y=80)
    drop.config(width = 25)
    # Create button, it will change label text
    show_button = Button(first_window,  bg='#607D8B' ,fg='black',borderwidth=3  ,text="Enter", command=show,width = 20)
    show_button.place(x=280,y=120)
    global ope
    strat_session_button = Button(first_window, bg='#607D8B' ,fg='black',borderwidth=3  ,text="Send session", width = 20,command=lambda:[start_session(),mass_box("Confirmation!",'Plan Sent Successfully ☑️'),Lb1.delete(0,END),operator()])
    strat_session_button.place(x=280,y=160)
    ttk.Label(first_window, text="Command Plan", background='black', foreground="white",
              font=("Times New Roman", 13)).place(x=410,y=570)
    ttk.Label(first_window, text="Received From Satellite", background='black', foreground="white",
              font=("Times New Roman", 13)).place(x=1550, y=5)
    ttk.Label(first_window, text="Progress", background='black', foreground="white",
              font=("Times New Roman", 13)).place(x=1420, y=570)
    ttk.Label(first_window, text="Image", background='black', foreground="white",
              font=("Times New Roman", 13)).place(x=1000, y=5)

    def delete_progress():
       Progress.delete('1.0', 'end')
    def delete_tlm():
        TLM.delete('1.0', 'end')
    def delete_image():
        canvas.delete('all')
    def show_imagee():
        canvas.create_image(20, 20, anchor=NW, image=immg)

    Lb1 = Listbox(first_window,border=2,width=159,height=28)
    Lb1.place(x=2,y=598)
    #scrollbar = Scrollbar(first_window)
    #scrollbar.place(x=676,y=32)
    #Lb1.config(yscrollcommand=scrollbar.set)
    #print(type(Lb1))
    #scrollbar.config(command=Lb1.yview)
    #scroll1=Scrollbar(orient=VERTICAL,width=50)
    #scroll1.place(x=610, y=20)
    #Lb1.config(yscrollcommand=scroll1.set)
    #scroll1.config(command=Lb1.yview)
    #scroll1.set(20, 200)
    ##scrollbar = Scrollbar(orient="vertical", command=Lb1.yview)
    ##scrollbar.pack(side="right", fill="y")
    ##Lb1.config(yscrollcommand=scrollbar.set)
    ##scrollbar.config(command=Lb1.yview)
    global TLM
    global Progress
    TLM=Text(first_window,height=31,border=2,width=73)
    TLM.place(x=1320,y=30)

    Progress=Text(first_window,border=2,width=116,height=28)
    Progress.place(x=980,y=598)

    clear_progress=Button(first_window, bg='#607D8B' ,fg='black',borderwidth=3  ,text="Clear", width = 5,height=5,command=delete_progress)
    clear_progress.place(x=1864,y=965)
    clear_tlm = Button(first_window, bg='#607D8B', fg='black', borderwidth=3, text="Clear", width=15,command=delete_tlm)
    clear_tlm.place(x=1550, y=536)
    show_image_button = Button(first_window, bg='#607D8B', fg='black', borderwidth=3, text="Show", width=15,command=show_imagee)
    show_image_button.place(x=885, y=536)
    clear_image_button = Button(first_window, bg='#607D8B', fg='black', borderwidth=3, text="Clear", width=15,command=delete_image)
    clear_image_button.place(x=1025, y=536)

    canvas = Canvas(first_window, width=600, height=480,border=2,bg='white')
    canvas.place(x=705,y=30)


    #imgg = PhotoImage(file="ima_600x480.jpg")



#-----------------End of the new window------------------------

# ----------------The welcome page----------------

# ----------------Execute tkinter-----------------

def server_program():
# -----------Start the New window module------------------
    print('in')
    global command_counter
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024
    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    try:
        server_socket.bind(('', port))  # bind host address and port together
    except:
        print('asdy')
    global ope
    print('ooopp : '+ope)
    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    global conn
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from Swarm Satellite is Established At : " + str(address))
    Beacon = conn.recv(1024).decode()

    print('Recevied Beacon From Swarm Satellite : ' + Beacon)
    with open('commandcounter.txt','w') as jo:
        jo.write(str(command_counter))
    print(ope)
    if ope=='go':
        print('iamima')
        while command_counter>0 :
            print(command_counter)
            start_session()
            command_counter-=1

    print('offf')
    server_socket.close()

def stablish():
    i=0
    print('in')
    global command_counter
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024
    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    try:
        server_socket.bind(('', port))  # bind host address and port together
    except:
        print('asdy')
    global ope
    print('ooopp : ' + ope)
    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    global conn
    conn, address = server_socket.accept()  # accept new connection
    #Lb2.insert(i,"Connection from Swarm Satellite is Established At : " + str(address))
    print("Connection from Swarm Satellite is Established At : " + str(address))
    Beacon = conn.recv(1024).decode()
    #Lb2.insert(i,'Recevied Beacon From Swarm Satellite : ' + Beacon)
    print('Recevied Beacon From Swarm Satellite : ' + Beacon)
    with open('commandcounter.txt', 'w') as jo:
        jo.write(str(command_counter))

img = PhotoImage(file="second pic.png")
label = Label(first_window,image=img)
label.place(x=0, y=30)
# ------------Activate delay function-------------
label2 = Label(first_window,command = delay())


def mass_boxx(x, y):
    messagebox.showinfo(x, y)
mass_boxx("Welocme",'The Program Wating For Connection To Be Established,Please Enter the IP in the next box')
IP = StringVar()
IP.set("192.168.1.1")
IP_input = Entry(first_window, width=3, textvariable=IP)

stablish()
#second_window.destroy()
def mass_boxxx(x, y):
    messagebox.showinfo(x, y)
mass_boxx("Confirmation!",'The Connection To Established Successfully ✔ ')
first_window.mainloop()

# -----------------End Program module-------------