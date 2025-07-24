# PLS-CADD Structure Strengths – Vectorial Sum
## When you have more than one (1) set in the same structure joint

Step-by-step guide:

- Set PLS-CADD: Criteria → Structure Loads Method 4  
- Extract PLS-CADD report: Lines → Reports → Structure Loads Report...  
  Right-click → Table View → Wire Loads In Structure Coordinate System For Structure Range  
  Copy and paste into your `.xlsx` file.
- Save your `.xlsx` file and this script in the same folder.
- Configure the Python script according to your needs.
- Run the script.
- ✨Magic✨

Once you have your report:

- Edit your Structure Loads Report: filter and delete the sets that were already added. Only keep the new sets.
- Paste the vectorial sum into your filtered Structure Loads Report.
- Run the other Python script that generates the Structure Loads Table.
