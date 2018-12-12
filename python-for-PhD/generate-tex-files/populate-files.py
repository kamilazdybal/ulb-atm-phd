# Generate and populate .tex files template

scalings = ['scale1', 'scale2']
centerings = ['center1', 'center2']
datas = ['100', '200']
dataalias = ['t100', 't200']
variables1 = ['Thing1', 'Thing2']
variables2 = ['Thing3', 'Thing4']

for index, data in enumerate(datas):
    for centering in centerings:
        for scaling in scalings:
            filename = data + '_cent_' + centering + '_scale_' + scaling + '.tex'
            print('Populating: ' + filename)
            file = open(filename, 'w+')

            file.write("\\subsection{" + dataalias[index] + ", Centering: " + centering + ", Scaling: " + scaling + "}\n\n\\begin{tabular}{cc}\n")

            for pc in range(1,7):
                if pc%2 == 1:
                    file.write("\t\t\\addheight{\\includegraphics[width=80mm]{cent_" + centering + "_scale_" + scaling + "_" + data + "_PC_" + str(pc) + ".eps}} &\n")
                else:
                    file.write("\t\t\\addheight{\\includegraphics[width=80mm]{cent_" + centering + "_scale_" + scaling + "_" + data + "_PC_" + str(pc) + ".eps}} \\\\" + "\n")

            file.write("\\end{tabular}\n\n\\begin{tabular}{cc}\n")

            file.write("\t\t\\addheight{\\includegraphics[width=80mm]{r2_cent_" + centering + "_scale_" + scaling + "_" + data + ".eps}} &\n")
            file.write("\t\t\\addheight{\\includegraphics[width=80mm]{rms_cent_" + centering + "_scale_" + scaling + "_" + data + ".eps}} \\\\\n")
            file.write("\\end{tabular}\n\n\\newpage\n\n\\begin{tabular}{cc}\n")

            for i, var in enumerate(variables1):
                if i%2 == 0:
                    file.write("\t\t\\addheight{\\includegraphics[width=80mm]{pp_" + var + "_cent_" + centering + "_scale_" + scaling + "_" + data + ".eps}} &\n")
                else:
                    file.write("\t\t\\addheight{\\includegraphics[width=80mm]{pp_" + var + "_cent_" + centering + "_scale_" + scaling + "_" + data + ".eps}} \\\\\n")

            file.write("\\end{tabular}\n\n\\begin{tabular}{cc}\n")

            for i, var in enumerate(variables2):
                if i%2 == 0:
                    file.write("\t\t\\addheight{\\includegraphics[width=80mm]{pp_" + var + "_cent_" + centering + "_scale_" + scaling + "_" + data + ".eps}} &\n")
                else:
                    file.write("\t\t\\addheight{\\includegraphics[width=80mm]{pp_" + var + "_cent_" + centering + "_scale_" + scaling + "_" + data + ".eps}} \\\\\n")
            file.write("\\end{tabular}\n\n")

            file.close()
