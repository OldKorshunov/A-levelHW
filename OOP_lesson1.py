class Element:#parent class with a method for determining the state of aggregation
    def agg_state(self, t):
        if t < self.t_melt:
            print("solid state")
        elif t >= self.t_melt and t < self.t_evaporation:
            print("Liquid state")
        else:
            print("Gaseous state")


class Oxygen(Element):
    t_melt = -218
    t_evaporation = -182


class Iron(Element):
    t_melt = 1538
    t_evaporation = 2862


class Chlorine(Element):
    t_melt = -100
    t_evaporation = -34


oxy = Oxygen()
iron = Iron()
chlor = Chlorine()


def switch():#меню выбора
   t=1
   while t != 0: 
       try: 
        t = int(input(" \nChlorine (агрегатное состояния хлора) => input 1; \nIron (агрегатное состояния железа) => input 2;\nOxygen (агрегатное состояния кислорода) => input 3; \nExit => input 0 \nEnter task number: ")) 
       except: 
        print("Incorrect! Print int number from 0 to 3!") 
       else: 
           if t == 1: 
            t = int(input("Enter a temperature of Chlorine: "))
            chlor.agg_state(t)#агрегатное состояния хлора
           elif t == 2: 
            t = int(input("Enter a temperature of Iron: "))
            iron.agg_state(t)#агрегатное состояния железа
           elif t == 3: 
            t = int(input("Enter a temperature of Oxygen: "))
            oxy.agg_state(t)#агрегатное состояния кислорода
           elif t == 0: 
            print("Exit...")#выход из программы
           else: 
            print("Wrong task!")

switch()