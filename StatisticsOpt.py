class Statistics_Operations:
    def __init__(self, liste):
        self.liste = liste

    def Sort(self, arr):
        if self.length(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.Sort(left) + middle + self.Sort(right)
    
    def length(self, arr=None):
        if arr is None:
            arr = self.liste
        sayac=0
        if arr==None:
            return 0
        else: 
            for i in arr:
                sayac+=1
            return sayac
        
        
    def Medyan(self):
        sorted_liste = self.Sort(self.liste)
        if self.length(sorted_liste)%2==0:
            mid_left=sorted_liste[(self.length(sorted_liste)//2)]
            mid_right=sorted_liste[self.length(sorted_liste)//2+1]
            return (mid_left+mid_right)/2
        else:
            return sorted_liste[self.length(sorted_liste)//2]

    def Ort(self):
        sum=0
        for i in self.liste:
            sum +=i
        return float((sum/self.length(self.liste)))    

    def Mod(self):
        mod_dict={}
        for i in self.liste:
           if i in mod_dict:
               mod_dict[i]+=1
           else:
               mod_dict[i]=1
               
        
        most_recurring=max(mod_dict.values())
        modes = [k for k, v in mod_dict.items() if v == most_recurring]
        return modes[0]
    
    def StDeviation(self):
        mean = float(self.Ort())
        stdeviation=1
        sayac=0
        variance=float(0)
        for item in self.liste:
            variance +=float((item-mean)**2)
            
        variance=float(variance/self.length(self.liste))
        
        while sayac<=variance:
            sayac +=1
            stdeviation=float(((variance/stdeviation)+stdeviation)/2)
            
        return stdeviation    
    
