#Simplified RC4
pt= "WHITEHAT"
k = [0,1,1,0,0,1,0,1,1,0,0,0,0,0,1,1]
s = [0,1,2,3,4,5,6,7] # shortening s array to 8 cells
j=0
# Key scheduling
for i in range(8):
    j=(j+s[i]+k[i]) % 8
    # swap
    temp = s[i]
    s[i] = s[j]
    s[j] = temp
# s = [1, 2, 4, 5, 0, 6, 7, 3]
i=0
j=0
keystream =[]
# Simplified Stream generation
for ch in pt:
    i = (i + 1) % 8
    j = (j+s[i]) % 8
    # swap
    temp = s[i]
    s[i] = s[j]
    s[j] = temp
    t = (s[i] + s[j]) % 8
    keystream.append(s[t])
print(keystream) # [7, 0, 5, 7, 2, 7, 5, 2]
# XOR Plaintext in binary with Key stream in binary
pt_ascii = [ord(char) for char in pt]
result = [pt_ascii[i] ^ keystream[i] 
          for i in range(min(len(pt_ascii), len(keystream)))]
# Convert binary to character
result_text = ''.join(chr(char) for char in result)
print(result_text) #PHLSGODV
