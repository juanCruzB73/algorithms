inp_string = 'Hello'
bytes_encoded = inp_string.encode()
print(type(bytes_encoded))
bythes_decoded = bytes_encoded.decode()
print(type(bythes_decoded))

def encode(strs: list[str]) -> str:
        res=''
        for word in strs:
            res+=str(len(word))+"#"+word
        return res

def decode(s: str) -> list[str]:
        res=[]
        index=0
        while(index<len(s)):
               j=index
               while(s[j]!="#"):
                      j+=1
               length=int(s[index:j])
               res.append(str(s[j+1:j+1+length]))
               index=j+1+length
        return res
               


arr=["neet","code","love","you"]
res=encode(arr)
print(res)
res2=decode(res)
print(res2)