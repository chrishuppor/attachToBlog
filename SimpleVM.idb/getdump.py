import idaapi

fw = open("c:\\users\\chris\\desktop\\SimpleVM_dump.hex", "wb")
beginea = 0x8048000
endea = 0x804c000
for i in range(0, endea - beginea):
	ea = beginea + i
	bytess=struct.pack('B',Byte(ea))
	fw.write(bytess)

fw.close()