
from enigma import Enigma, I, II, III, IV, V, B, C
from analysis import brute

if __name__ == '__main__':
    E = Enigma([II, V, III], B, 'AF-TN-KO-BL-RW', [{8}, {4}, {19}], [1, 14, 21])
    p = 'IPROPOSETOCONSIDERTHEQUESTIONCANMACHINESTHINKTHISSHOULDBEGINWITHDEFINITIONSOFTHEMEANINGOFTHETERMSMACHINEANDTHINKTHEDEFINITIONSMIGHTBEFRAMEDSOASTOREFLECTSOFARASPOSSIBLETHENORMALUSEOFTHEWORDSBUTTHISATTITUDEISDANGEROUSIFTHEMEANINGOFTHEWORDSMACHINEANDTHINKARETOBEFOUNDBYEXAMININGHOWTHEYARECOMMONLYUSEDITISDIFFICULTTOESCAPETHECONCLUSIONTHATTHEMEANINGANDTHEANSWERTOTHEQUESTIONCANMACHINESTHINKISTOBESOUGHTINASTATISTICALSURVEYSUCHASAGALLUPPOLLBUTTHISISABSURDINSTEADOFATTEMPTINGSUCHADEFINITIONISHALLREPLACETHEQUESTIONBYANOTHERWHICHISCLOSELYRELATEDTOITANDISEXPRESSEDINRELATIVELYUNAMBIGUOUSWORDS'
    c = E(p)
    
    c = 'feogi vevek aggah egwxc iepng qjrxs nmkxp ygcje xkmiw kcgqa qtofp dwxky lsnrp aqrmp opyel dpkff jlfwd svbcj bvutz tuofp uzwmu vcmyz qjmlq sagpi llglr lilpg ojjrb rdygp iyink ewrmp qpbug oylbb voqmh hpmws uwhxe cqkyr kncxz eskdt kklvk jhpif sbsig murpy dvrih kzedb ashmm onkql yfscs nmyyx batqw chaia arpgp fjijy rruhx ebvmg trgxc vwuqg fgnui nsfub lbicn oohzz iymws wtwuk wvcyh rirnq apccp gbyye gkbhs onaqb wuuju ossca qnbke ctmfz thuru dakyv eolzl wurbw zvpeq rbgcb khhsp huznk kthny dhcbj dgxhc btias rsvck yiofj hmwmg tahis hcwhf fatko whfsl tfncm nvlwk pcabl bnfxv aiote ioeuc pdjvk mwjjn qhopz umkkj ykkwt ideud teqto layfr tuoxv bgtwc hugld cldwc gvivh isvqg kzupo vkisq vapox vyits irtwv hfxj'.upper().replace(' ', '')
    rotors, reflector, plugboard, restarts, offsets = brute(c, [I, II, III], 3, B, 5)
    
    pp = Enigma(rotors, reflector, plugboard, restarts, offsets)(c)
    
    print('=== Resulting plaintextish ===')
    print(pp)
    print('')
    print('=== Diff ===')
    print(''.join(x if x == y else '-' for x, y in zip(p, pp)))

