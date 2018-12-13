# Populate .tex file with graphs

scalings = ['scale1', 'scale2']
centerings = ['center1', 'center2']

filename = 'combined.tex'
print('Populating: ' + filename)
file = open(filename, 'w+')

for centering in centerings:
    for scaling in scalings:
        file.write("\\subsection{Combined, Centering: " + centering + ", Scaling: " + scaling + "}\n\n\\begin{tabular}{cc}\n")

        for pc in range(1,7):
            if pc%2 == 1:
                file.write("\t\t\\addheight{\\includegraphics[width=80mm]{combined_cent_" + centering + "_scale_" + scaling + "_PC_" + str(pc) + ".eps}} &\n")
            else:
                file.write("\t\t\\addheight{\\includegraphics[width=80mm]{combined_cent_" + centering + "_scale_" + scaling + "_PC_" + str(pc) + ".eps}} \\\\" + "\n")

        file.write("\\end{tabular}\n\n\\newpage\n\n")

file.close()
