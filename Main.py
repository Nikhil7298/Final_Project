from functions import Functions
class Final:
  def executing(choice):
    if choice==1:
        print('****ADD FOOD****')
        OBJ.ADDFOOD()
    if choice==2:
        print('****VIEW FOOD****')
        OBJ.view()
    if choice==3:
        print('****UPDATE FOOD****')
        OBJ.Update()

obj=Final()
OBJ=Functions()
while True:
    choice=int(input('Enter\n 1.ADD FOOD\n 2.VIEW FOOD\n 3.EDIT FOOD\n '))
    Final.executing(choice)
    

    