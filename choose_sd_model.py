
import subprocess
import os
import platform

if platform.system() != "Windows":
    sd_python_path=os.path.join(".", "model_conv/bin/python3")
    chose_model=os.path.join(os.path.dirname(__file__), "sd_model_conversion.py")
else:
    sd_python_path=r'model_conv\Scripts\python.exe'
    chose_model=r'openvino-ai-plugins-gimp\sd_model_conversion.py'

print("=========Chose SD-1.5 models to download and convert=========")
print("1 - Square (512x512 output image) ")
print("2 - Landscape (640x360 output image, 16:9) ")	
print("3 - Portrait (360x640 output image, 9:16) ")
print("4 - Portrait_512x768 (512x768 output image), will take time since model is large ")
print("5 - Landscape_768x512 (768x512 output image),  will take time since model is large ")
print("6 - SD-1.5 Inapinting model (512x512 output image) ")
print("7 - ALL the above SD-1.5 models ")
print("8 - Only Square, Landscape, Portrait")
print("9 - Skip All SD-1.5 Model setup ")   
    
while True:
    choice = input("Enter the Number for the model you want to download & convert: ")

    # setup all the SD1.5 models
    if choice=="7":
        for i in range(1,7):
            
            subprocess.call([sd_python_path, chose_model, str(i)])
            
        break
    # setup only square, landscape and Portrait
    elif choice=="8":
        for i in range(1,4):
       
            subprocess.call([sd_python_path, chose_model, str(i)])
        break
    elif choice=="9":
        print("Exiting SD-1.5 Model setup.........")
        break
    elif choice in ["1","2","3","4","5","6"]:
      
        subprocess.call([sd_python_path, chose_model, choice])
    
        break
  
    else:
        print("Wrong option selected.")
        
			
    


    
    
    
