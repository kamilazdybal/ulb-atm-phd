# Generate and populate `.tex` files

This is a Python template that can be adjusted to generate and populate `.tex` files with content.

As it is, it is mostly suitable to adjust for populating with figures that have some pattern to their filenames.

Then, in your master `.tex` file you can `\input{}` the populated files.

**Note: These Python scripts will overwrite files with every run!**

## Example output inside `.tex` file

```
  \subsection{t100, Centering: center1, Scaling: scale1}

  \begin{tabular}{cc}
  		\addheight{\includegraphics[width=80mm]{cent_center1_scale_scale1_100_PC_1.eps}} &
  		\addheight{\includegraphics[width=80mm]{cent_center1_scale_scale1_100_PC_2.eps}} \\
  		\addheight{\includegraphics[width=80mm]{cent_center1_scale_scale1_100_PC_3.eps}} &
  		\addheight{\includegraphics[width=80mm]{cent_center1_scale_scale1_100_PC_4.eps}} \\
  		\addheight{\includegraphics[width=80mm]{cent_center1_scale_scale1_100_PC_5.eps}} &
  		\addheight{\includegraphics[width=80mm]{cent_center1_scale_scale1_100_PC_6.eps}} \\
  \end{tabular}

  \begin{tabular}{cc}
  		\addheight{\includegraphics[width=80mm]{r2_cent_center1_scale_scale1_100.eps}} &
  		\addheight{\includegraphics[width=80mm]{rms_cent_center1_scale_scale1_100.eps}} \\
  \end{tabular}

  \newpage

  \begin{tabular}{cc}
  		\addheight{\includegraphics[width=80mm]{pp_Thing1_cent_center1_scale_scale1_100.eps}} &
  		\addheight{\includegraphics[width=80mm]{pp_Thing2_cent_center1_scale_scale1_100.eps}} \\
  \end{tabular}

  \begin{tabular}{cc}
  		\addheight{\includegraphics[width=80mm]{pp_Thing3_cent_center1_scale_scale1_100.eps}} &
  		\addheight{\includegraphics[width=80mm]{pp_Thing4_cent_center1_scale_scale1_100.eps}} \\
  \end{tabular}
```

## File generation with only a bash script

Here is a template of a `.bash` script to `touch` files just in case you have something unique that needs to be populated by hand.

Note: No need to `touch` files with the above Python scripts, since Python will generate the files anyway if they don't yet exist.

```
#!/bin/bash
DATAALIAS="100"
CENTERING="center1"

touch "$DATAALIAS""_cent_$CENTERING"".tex"
touch "$DATAALIAS""_cent_$CENTERING"".tex"
touch "$DATAALIAS""_cent_$CENTERING"".tex"
touch "$DATAALIAS""_cent_$CENTERING"".tex"
touch "$DATAALIAS""_cent_$CENTERING"".tex"
touch "$DATAALIAS""_cent_$CENTERING"".tex"
touch "comparison_cent_$CENTERING"".tex"
```
