class BinarySearch(list):
    #create a class BinarySearch
    def __init__(self,x,y):
      data=[]
      data.append(y)
      list_len=1
      while list_len<x:
        data.append(data[list_len-1]+y)
        list_len+=1
      super(BinarySearch,self).__init__(data)
      self.length=len(data)

    def search(self,number):
        count=0
        first=0
        self.length=len(self)
        last=self.length-1
        mid_point=int((last)/2)
        position={'count':'','index':''}
        while first<mid_point:
            
            if (first==mid_point) and (self[first]>number):
                index=-1 
                position["count"]=self.length
                position["index"]=index
                return position
            
            elif self[first]==number:
                index=first
                position["count"]=count
                position["index"]=index
                return position
            elif self[last]==number:
                index=last
                position["count"]=count
                position["index"]=index
                return position
            elif self[mid_point]==number:
                index=mid_point
                position["count"]=count
                position["index"]=index
                return position
            else:
                if self[mid_point]>number:
                    last=mid_point-1
                    first=first+1
                    mid_point=(last + first)//2
                else:
                    first=mid_point + 1
                    last=last - 1
                    mid_point=((last + first)//2)+1
            count+=1
        position={'count':count,'index':-1}       
        return position