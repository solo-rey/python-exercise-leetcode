"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

Note:
The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.
Show Company Tags
Show Tags
Show Similar Problems

"""

class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return None
        return "\#\#\#".join(strs)



    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        # if not s:
        #     return []
        if s == '':
            return  ['']
        if s is None:
            return []
        return s.split("\#\#\#")


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
s = ["tq[&u%u<VgO3_nW3L@:Gj={z|V\"\"\"8+1N0e,q$E7d^C#Hkib&1qt^]_eDH-N*!gj<~&u*u1*~MMSy|hr[=q5**L8hO<:Lr=9GCbapYaAw=F$#.",
     "H?.gljV6D?Q[gIO.}]oBNs(i6v29X.E*lu=","^J7SwU.Naw#~_Y7ubLvSC+4u$cA!bxQxgZ7~5;M|T!zI}$Sv!5YvIA}u*E(;&N/N;$x~x=jelcdS(@}vD[9J!gE9<I;=d%MK+vEpvP7pUM{nE;<Q1DN2BvAn|8J*lYt-xja#(^tFw0x@_nd<;?:*z(<bdXxC9$Km]~HA$.G7/g",
     "e=B)k3j+j6A/[AcGl]<Jp3k&Xc<<l=*W5giYnZT5,D]|pa#9YRKi?c*+!q$?6e4&!L.S*v[YweuTUm&%q=[z}H6jkjDhM2|A|` GkX39Uo;<1o}zWI.@$-bqWsYON[wxTPN",
     "QGuz<YY;rUtc8{=.yuRT]~)1;Os~6YjFI(H%NR,)*Ci-mobOZT)i/KNBLiYEHc2KTT)_NQRnf=])P&xxrG]Zek[(V5}tnt9PrmNSel(({Rxfjae?ED 0NDW7bYa9E!52i_C}?:! (0=9w9QD[,}",
     "(_#y|s,n2]^R*NBT.dp}Ja` >|mR3lxi-@&B X_<:t.]mt/nJ}8XC{0m)]7 :i/}$,eJG^)sC:FvoxQW?*I}",
     "k[yb=U16ilu(]4bpor#K96C|xY[P~HhH jmpidKGJ[tgnMIbkVj;Aw`T.hd}|w",
     ";T`afc<YMoJ"]

codec = Codec()
# a = codec.encode(s)
# t = a.split("###")

print codec.decode(codec.encode([""]))
print codec.decode(codec.encode([]))
