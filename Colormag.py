import xlrd
import matplotlib.pyplot as plt
import math 

from xlrd import open_workbook


bench = open_workbook('/Users/adbreeze13/Desktop/UNCResearch/Test/finaldata.xlsx',on_demand=True)

appmagcol1 = []
bp_rpcol2 = []
parallaxcol3 = []
poecol4 = []
gfloecol5 = []
bpfloecol6 = []
rpfloecol7 = []
absmag = []


for name in bench.sheet_names():
    sheetnew = bench.sheet_by_name(name)
    for row in range(0, 100000):
        
        appmagcoltype = sheetnew.cell_type(row, 0)
        bp_rpcoltype = sheetnew.cell_type(row, 1)
        parallaxcoltype = sheetnew.cell_type(row, 2)
        poecoltype = sheetnew.cell_type(row, 3)
        gfloecoltype = sheetnew.cell_type(row, 4)
        bpfloecoltype = sheetnew.cell_type(row, 5)
        rpfloecoltype = sheetnew.cell_type(row, 6)
        
        if not appmagcoltype == xlrd.XL_CELL_EMPTY and not bp_rpcoltype == xlrd.XL_CELL_EMPTY and not parallaxcoltype == xlrd.XL_CELL_EMPTY and not poecoltype == xlrd.XL_CELL_EMPTY and not gfloecoltype == xlrd.XL_CELL_EMPTY and not bpfloecoltype == xlrd.XL_CELL_EMPTY and not rpfloecoltype == xlrd.XL_CELL_EMPTY:
            if sheetnew.cell_value(row, 3) > 20 and sheetnew.cell_value(row, 4) > 20 and sheetnew.cell_value(row, 5) > 20 and sheetnew.cell_value(row,6) > 20:
                appmagcol1.append(sheetnew.cell_value(row, 0))
                bp_rpcol2.append(sheetnew.cell_value(row, 1))
                parallaxcol3.append(sheetnew.cell_value(row,2))
                poecol4.append(sheetnew.cell_value(row, 3))
                gfloecol5.append(sheetnew.cell_value(row, 4))
                bpfloecol6.append(sheetnew.cell_value(row, 5))
                rpfloecol7.append(sheetnew.cell_value(row, 6))

        

        


for i in range(len(appmagcol1)):
    abscalc = appmagcol1[i]-(5*math.log((1000/parallaxcol3[i]), 10))+5
    absmag.append(abscalc)




        
plt.scatter(bp_rpcol2, absmag, s=.01)
plt.xlabel('Bp-Rp')
plt.ylabel('Absolute Magnitude')
plt.gca().invert_yaxis()
plt.title('Color-Magnitude Diagram')
plt.show()








