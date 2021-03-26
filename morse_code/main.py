alfabet ={
    "A":"• —",
    "B":"— • • •",
    "C":"— • — •",
    "D":"— • •",
    "E":"•",
    "F":"• • — •",
    "G":"— — •",
    "H":"• • • •",
    "I":"• •",
    "J":"• — — —",
    "K":"— • —",
    "L":"• — • •",
    "M":"— —",
    "N":"— •",
    "O":"— — —",
    "P":"• — — •",
    "Q":"— — • —",
    "R":"• — •",
    "S":"• • •",
    "T":"—",
    "U":"• • —",
    "V":"• • • —",
    "W":"• — —",
    "X":"— • • —",
    "Y":"— • — —",
    "Z":"— — • •"
}

slowo = str(input("Podaj slowo: "))
slowo= slowo.upper()
print(slowo)
for litera in slowo:
    print(alfabet[litera])
