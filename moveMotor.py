import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
RPiPins=[35,37,36,38]
for pin in RPiPins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,False)
 
Step_Seq_Num=0
Rot_Spd=.001
Rotate=4096
Rotate_Dir=1
spin = 4000
 
Step_Seq=[[1,0,0,0],
          [1,1,0,0],
          [0,1,0,0],
          [0,1,1,0],
          [0,0,1,0],
          [0,0,1,1],
          [0,0,0,1],
          [1,0,0,1]]
RotateF=float(input('Number of revolutions: ')) / 10
Rotate_Dir =input('Direction (1 or -1)')
Rot_Spd = (input('Speed (1-0.00)'))
Rotate=int(RotateF*spin)
if Rotate<1:Rotate=spin
Rotate_Dir = int(Rotate_Dir)
if Rotate_Dir!=1 and Rotate_Dir!=-1: Rotate_Dir=1
Rot_Spd=float(Rot_Spd)
if Rot_Spd>1 or Rot_Spd<.001:Rot_Spd=.001
print(Rotate,Rotate_Dir,Rot_Spd)
 
for x in range(0,(Rotate+1)):
    for pin in range(0,4):
        Pattern_Pin=RPiPins[pin]
        if Step_Seq[Step_Seq_Num][pin]==1:
            GPIO.output(Pattern_Pin,True)
        else:
            GPIO.output(Pattern_Pin,False)
    Step_Seq_Num+=Rotate_Dir
    if(Step_Seq_Num>=8):
        Step_Seq_Num=0
    elif(Step_Seq_Num<0):
        Step_Seq_Num=7
    time.sleep(Rot_Spd)
GPIO.cleanup()
print('Done')
