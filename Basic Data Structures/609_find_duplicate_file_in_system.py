class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic=defaultdict(lambda :[])
        for i in range(len(paths)):
            st=paths[i]
            lst=st.split(" ")
            for j in range(1,len(lst)):
                sp=lst[j].index("(")
                dic[lst[j][sp:]].append(lst[0]+"/"+lst[j][:sp])
        return [dic[i] for i in dic if len(dic[i])>1]

    def findDuplicate_another(self, paths: List[str]) -> List[List[str]]:
        dic={}
        for i in paths:
            for j in range(len(i)):
                if i[j]==' ':
                    path=i[:j]
                    break
            content=''  
            file=i[j:]  
            print(path)
            while file:
                s=file.find('(')
                e=file.find(')')
                filen=file[1:s]
                content=file[s+1:e]
                file=file[e+1:]
                if content in dic:
                    dic[content].append(path+'/'+filen)
                else:
                    dic[content]=[path+'/'+filen]  
        l=[i for i in dic.values() if len(i)>1]
        l.reverse()
        return l