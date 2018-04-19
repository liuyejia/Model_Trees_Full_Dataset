import csv

leafnode = []
pred_per = []
position_list_1 = ['Small Forward', 'Point Guard and Shooting Guard and Small Forward', 
                   'Power Forward and Shooting Guard and Small Forward', 'Power Forward', 
                   'Small Forward and Point Guard and Shooting Guard', 
                   'Small Forward and Power Forward', 'Point Guard', 
                   'Shooting Guard and Small Forward and Point Guard', 
                   'Point Guard and Shooting Guard', 'Small Forward and Shooting Guard', 
                   'Small Forward and Shooting Guard and Power Forward', 'Small Forward and Power Forward and Center', 
                   'Shooting Guard and Power Forward', 'Power Forward and Small Forward', 
                   'Shooting Guard and Point Guard', 'Shooting Guard and Small Forward', 
                   'Shooting Guard and Small Forward and Power Forward', 'Center and Power Forward', 
                   'Power Forward and Center', 'Point Guard and Small Forward and Shooting Guard', 
                   'Small Forward and Power Forward and Shooting Guard', 'Small Forward and Shooting Guard and Point Guard', 
                   'Center and Small Forward and Power Forward', 'Power Forward and Center and Small Forward', 
                   'Small Forward and Center and Power Forward', 'Center and Power Forward and Small Forward', 
                   'Shooting Guard and Power Forward and Small Forward']

position_list_2 = ['Center/Forward', 'Center and Small Forward', 
                   'Small Forward and Center', 'Center', 'Shooting Guard and Point Guard and Small Forward',
                   'Power Forward and Small Forward and Shooting Guard', 'Shooting Guard',
                   'Small Forward,Point Guard and Shooting Guard and Small Forward', 
                   'Power Forward and Shooting Guard and Small Forward', 'Power Forward',
                   'Small Forward and Point Guard and Shooting Guard',
                   'Small Forward and Power Forward', 'Point Guard', 
                   'Shooting Guard and Small Forward and Point Guard', 'Point Guard and Shooting Guard',
                   'Small Forward and Shooting Guard', 'Small Forward and Shooting Guard and Power Forward',
                   'Small Forward and Power Forward and Center', 'Shooting Guard and Power Forward', 
                   'Power Forward and Small Forward', 'Shooting Guard and Point Guard',
                   'Shooting Guard and Small Forward', 'Shooting Guard and Small Forward and Power Forward',
                   'Center and Power Forward', 'Power Forward and Center',
                   'Point Guard and Small Forward and Shooting Guard', 'Small Forward and Power Forward and Shooting Guard',
                   'Small Forward and Shooting Guard and Point Guard', 'Center and Small Forward and Power Forward',
                   'Power Forward and Center and Small Forward', 'Small Forward and Center and Power Forward',
                   'Center and Power Forward and Small Forward', 'Shooting Guard and Power Forward and Small Forward'] 

position_leaf1_1 = ['Center/Forward', 'Center and Small Forward', 
                    'Small Forward and Center', 'Center', 'Shooting Guard and Point Guard and Small Forward',
                    'Power Forward and Small Forward and Shooting Guard', 'Shooting Guard', 'Small Forward',
                    'Point Guard and Shooting Guard and Small Forward', 
                    'Power Forward and Shooting Guard and Small Forward', 'Power Forward', 
                    'Small Forward and Point Guard and Shooting Guard', 'Small Forward and Power Forward',
                    'Point Guard', 'Shooting Guard and Small Forward and Point Guard',
                    'Point Guard and Shooting Guard', 'Small Forward and Shooting Guard', 
                    'Small Forward and Shooting Guard and Power Forward',
                    'Small Forward and Power Forward and Center', 'Shooting Guard and Power Forward',
                    'Power Forward and Small Forward', 'Shooting Guard and Point Guard', 
                    'Shooting Guard and Small Forward', 'Shooting Guard and Small Forward and Power Forward', 'Center and Power Forward',
                    'Power Forward and Center', 'Point Guard and Small Forward and Shooting Guard', 'Small Forward and Power Forward and Shooting Guard',
                    'Small Forward and Shooting Guard and Point Guard', 'Center and Small Forward and Power Forward', 
                    'Power Forward and Center and Small Forward', 'Small Forward and Center and Power Forward',
                    'Center and Power Forward and Small Forward', 'Shooting Guard and Power Forward and Small Forward']

position_leaf1_2 = ['Point Guard and Shooting Guard and Small Forward',
                    'Power Forward and Shooting Guard and Small Forward',
                    'Power Forward', 'Small Forward and Point Guard and Shooting Guard',
                    'Small Forward and Power Forward', 'Point Guard', 'Shooting Guard and Small Forward and Point Guard',
                    'Point Guard and Shooting Guard', 'Small Forward and Shooting Guard',
                    'Small Forward and Shooting Guard and Power Forward', 'Small Forward and Power Forward and Center', 
                    'Shooting Guard and Power Forward', 'Power Forward and Small Forward', 'Shooting Guard and Point Guard',
                    'Shooting Guard and Small Forward', 'Shooting Guard and Small Forward and Power Forward',
                    'Center and Power Forward', 'Power Forward and Center', 'Point Guard and Small Forward and Shooting Guard',
                    'Small Forward and Power Forward and Shooting Guard', 'Small Forward and Shooting Guard and Point Guard',
                    'Center and Small Forward and Power Forward', 'Power Forward and Center and Small Forward', 'Small Forward and Center and Power Forward',
                    'Center and Power Forward and Small Forward', 'Shooting Guard and Power Forward and Small Forward']

position_leaf1_3 = ['Center and Power Forward', 'Power Forward and Center',
                    'Point Guard and Small Forward and Shooting Guard', 'Small Forward and Power Forward and Shooting Guard',
                    'Small Forward and Shooting Guard and Point Guard', 'Center and Small Forward and Power Forward',
                    'Power Forward and Center and Small Forward', 'Small Forward and Center and Power Forward',
                    'Center and Power Forward and Small Forward', 'Shooting Guard and Power Forward and Small Forward']

position_leaf2_1 = ['Center/Forward', 'Center and Small Forward',
                    'Small Forward and Center', 'Center', 'Shooting Guard and Point Guard and Small Forward',
                    'Power Forward and Small Forward and Shooting Guard', 'Shooting Guard',
                    'Small Forward', 'Point Guard and Shooting Guard and Small Forward',
                    'Power Forward and Shooting Guard and Small Forward', 'Power Forward',
                    'Small Forward and Point Guard and Shooting Guard', 'Small Forward and Power Forward',
                    'Point Guard', 'Shooting Guard and Small Forward and Point Guard',
                    'Point Guard and Shooting Guard', 'Small Forward and Shooting Guard', 'Small Forward and Shooting Guard and Power Forward',
                    'Small Forward and Power Forward and Center', 'Shooting Guard and Power Forward',
                    'Power Forward and Small Forward', 'Shooting Guard and Point Guard', 'Shooting Guard and Small Forward',
                    'Shooting Guard and Small Forward and Power Forward', 'Center and Power Forward',
                    'Power Forward and Center', 'Point Guard and Small Forward and Shooting Guard',
                    'Small Forward and Power Forward and Shooting Guard', 'Small Forward and Shooting Guard and Point Guard',
                    'Center and Small Forward and Power Forward', 'Power Forward and Center and Small Forward',
                    'Small Forward and Center and Power Forward', 'Center and Power Forward and Small Forward', 
                    'Shooting Guard and Power Forward and Small Forward']

position_leaf2_2 = ['Point Guard and Shooting Guard and Small Forward', 'Power Forward and Shooting Guard and Small Forward',
                    'Power Forward', 'Small Forward and Point Guard and Shooting Guard',
                    'Small Forward and Power Forward', 'Point Guard', 'Shooting Guard and Small Forward and Point Guard',
                    'Point Guard and Shooting Guard', 'Small Forward and Shooting Guard', 'Small Forward and Shooting Guard and Power Forward',
                    'Small Forward and Power Forward and Center', 'Shooting Guard and Power Forward',
                    'Power Forward and Small Forward', 'Shooting Guard and Point Guard',
                    'Shooting Guard and Small Forward', 'Shooting Guard and Small Forward and Power Forward',
                    'Center and Power Forward', 'Power Forward and Center', 'Point Guard and Small Forward and Shooting Guard',
                    'Small Forward and Power Forward and Shooting Guard',
                    'Small Forward and Shooting Guard and Point Guard', 'Center and Small Forward and Power Forward',
                    'Power Forward and Center and Small Forward', 'Small Forward and Center and Power Forward',
                    'Center and Power Forward and Small Forward', 'Shooting Guard and Power Forward and Small Forward']
position_leaf2_3 = ['Center and Power Forward', 'Power Forward and Center',
                    'Point Guard and Small Forward and Shooting Guard', 'Small Forward and Power Forward and Shooting Guard',
                    'Small Forward and Shooting Guard and Point Guard', 'Center and Small Forward and Power Forward',
                    'Power Forward and Center and Small Forward', 'Small Forward and Center and Power Forward',
                    'Center and Power Forward and Small Forward', 'Shooting Guard and Power Forward and Small Forward']

position_leaf3_1 = ['Center/Forward', 'Center and Small Forward',
                    'Small Forward and Center', 'Center', 'Shooting Guard and Point Guard and Small Forward',
                    'Power Forward and Small Forward and Shooting Guard', 'Shooting Guard',
                    'Small Forward', 'Point Guard and Shooting Guard and Small Forward',
                    'Power Forward and Shooting Guard and Small Forward',
                    'Power Forward', 'Small Forward and Point Guard and Shooting Guard',
                    'Small Forward and Power Forward', 'Point Guard', 'Shooting Guard and Small Forward and Point Guard',
                    'Point Guard and Shooting Guard', 'Small Forward and Shooting Guard',
                    'Small Forward and Shooting Guard and Power Forward',
                    'Small Forward and Power Forward and Center', 'Shooting Guard and Power Forward',
                    'Power Forward and Small Forward', 'Shooting Guard and Point Guard',
                    'Shooting Guard and Small Forward', 'Shooting Guard and Small Forward and Power Forward',
                    'Center and Power Forward', 'Power Forward and Center', 'Point Guard and Small Forward and Shooting Guard',
                    'Small Forward and Power Forward and Shooting Guard', 'Small Forward and Shooting Guard and Point Guard',
                    'Center and Small Forward and Power Forward', 'Power Forward and Center and Small Forward',
                    'Small Forward and Center and Power Forward', 'Center and Power Forward and Small Forward',
                    'Shooting Guard and Power Forward and Small Forward']

position_leaf3_2 = ['Point Guard and Shooting Guard and Small Forward', 'Power Forward and Shooting Guard and Small Forward',
                    'Power Forward', 'Small Forward and Point Guard and Shooting Guard',
                    'Small Forward and Power Forward', 'Point Guard', 'Shooting Guard and Small Forward and Point Guard',
                    'Point Guard and Shooting Guard', 'Small Forward and Shooting Guard',
                    'Small Forward and Shooting Guard and Power Forward', 'Small Forward and Power Forward and Center',
                    'Shooting Guard and Power Forward', 'Power Forward and Small Forward', 'Shooting Guard and Point Guard',
                    'Shooting Guard and Small Forward', 'Shooting Guard and Small Forward and Power Forward',
                    'Center and Power Forward', 'Power Forward and Center', 'Point Guard and Small Forward and Shooting Guard',
                    'Small Forward and Power Forward and Shooting Guard', 'Small Forward and Shooting Guard and Point Guard',
                    'Center and Small Forward and Power Forward', 'Power Forward and Center and Small Forward', 
                    'Small Forward and Center and Power Forward', 'Center and Power Forward and Small Forward',
                    'Shooting Guard and Power Forward and Small Forward']

position_leaf3_3 = ['Center and Power Forward', 'Power Forward and Center',
                    'Point Guard and Small Forward and Shooting Guard', 'Small Forward and Power Forward and Shooting Guard',
                    'Small Forward and Shooting Guard and Point Guard', 'Center and Small Forward and Power Forward',
                    'Power Forward and Center and Small Forward', 'Small Forward and Center and Power Forward',
                    'Center and Power Forward and Small Forward', 'Shooting Guard and Power Forward and Small Forward']

position_leaf4_1 = ['Center/Forward', 'Center and Small Forward',
                    'Small Forward and Center', 'Center', 'Shooting Guard and Point Guard and Small Forward',
                    'Power Forward and Small Forward and Shooting Guard', 'Shooting Guard',
                    'Small Forward', 'Point Guard and Shooting Guard and Small Forward',
                    'Power Forward and Shooting Guard and Small Forward', 'Power Forward',
                    'Small Forward and Point Guard and Shooting Guard', 'Small Forward and Power Forward',
                    'Point Guard', 'Shooting Guard and Small Forward and Point Guard',
                    'Point Guard and Shooting Guard', 'Small Forward and Shooting Guard',
                    'Small Forward and Shooting Guard and Power Forward', 'Small Forward and Power Forward and Center',
                    'Shooting Guard and Power Forward', 'Power Forward and Small Forward', 'Shooting Guard and Point Guard',
                    'Shooting Guard and Small Forward', 'Shooting Guard and Small Forward and Power Forward',
                    'Center and Power Forward,Power Forward and Center', 'Point Guard and Small Forward and Shooting Guard',
                    'Small Forward and Power Forward and Shooting Guard', 'Small Forward and Shooting Guard and Point Guard',
                    'Center and Small Forward and Power Forward', 'Power Forward and Center and Small Forward',
                    'Small Forward and Center and Power Forward', 'Center and Power Forward and Small Forward',
                    'Shooting Guard and Power Forward and Small Forward']

position_leaf4_2 = ['Point Guard and Shooting Guard and Small Forward', 'Power Forward and Shooting Guard and Small Forward',
                    'Power Forward', 'Small Forward and Point Guard and Shooting Guard',
                    'Small Forward and Power Forward', 'Point Guard', 'Shooting Guard and Small Forward and Point Guard',
                    'Point Guard and Shooting Guard', 'Small Forward and Shooting Guard',
                    'Small Forward and Shooting Guard and Power Forward', 'Small Forward and Power Forward and Center',
                    'Shooting Guard and Power Forward', 'Power Forward and Small Forward', 
                    'Shooting Guard and Point Guard', 'Shooting Guard and Small Forward', 
                    'Shooting Guard and Small Forward and Power Forward', 'Center and Power Forward',
                    'Power Forward and Center', 'Point Guard and Small Forward and Shooting Guard',
                    'Small Forward and Power Forward and Shooting Guard', 'Small Forward and Shooting Guard and Point Guard',
                    'Center and Small Forward and Power Forward', 'Power Forward and Center and Small Forward', 
                    'Small Forward and Center and Power Forward', 'Center and Power Forward and Small Forward',
                    'Shooting Guard and Power Forward and Small Forward']

position_leaf4_3 = ['Center and Power Forward', 'Power Forward and Center',
                    'Point Guard and Small Forward and Shooting Guard', 'Small Forward and Power Forward and Shooting Guard',
                    'Small Forward and Shooting Guard and Point Guard', 'Center and Small Forward and Power Forward',
                    'Power Forward and Center and Small Forward', 'Small Forward and Center and Power Forward',
                    'Center and Power Forward and Small Forward', 'Shooting Guard and Power Forward and Small Forward']

position_leaf5_1 = ['Center/Forward', 'Center and Small Forward',
                    'Small Forward and Center', 'Center', 'Shooting Guard and Point Guard and Small Forward',
                    'Power Forward and Small Forward and Shooting Guard', 'Shooting Guard',
                    'Small Forward', 'Point Guard and Shooting Guard and Small Forward',
                    'Power Forward and Shooting Guard and Small Forward', 'Power Forward',
                    'Small Forward and Point Guard and Shooting Guard', 'Small Forward and Power Forward',
                    'Point Guard', 'Shooting Guard and Small Forward and Point Guard',
                    'Point Guard and Shooting Guard', 'Small Forward and Shooting Guard',
                    'Small Forward and Shooting Guard and Power Forward', 'Small Forward and Power Forward and Center',
                    'Shooting Guard and Power Forward', 'Power Forward and Small Forward', 
                    'Shooting Guard and Point Guard', 'Shooting Guard and Small Forward', 'Shooting Guard and Small Forward and Power Forward',
                    'Center and Power Forward', 'Power Forward and Center', 'Point Guard and Small Forward and Shooting Guard',
                    'Small Forward and Power Forward and Shooting Guard', 'Small Forward and Shooting Guard and Point Guard',
                    'Center and Small Forward and Power Forward', 'Power Forward and Center and Small Forward',
                    'Small Forward and Center and Power Forward', 'Center and Power Forward and Small Forward',
                    'Shooting Guard and Power Forward and Small Forward']

position_leaf5_2 = ['Point Guard and Shooting Guard and Small Forward', 'Power Forward and Shooting Guard and Small Forward',
                    'Power Forward', 'Small Forward and Point Guard and Shooting Guard',
                    'Small Forward and Power Forward', 'Point Guard', 'Shooting Guard and Small Forward and Point Guard',
                    'Point Guard and Shooting Guard', 'Small Forward and Shooting Guard',
                    'Small Forward and Shooting Guard and Power Forward', 'Small Forward and Power Forward and Center',
                    'Shooting Guard and Power Forward', 'Power Forward and Small Forward', 'Shooting Guard and Point Guard', 
                    'Shooting Guard and Small Forward', 'Shooting Guard and Small Forward and Power Forward',
                    'Center and Power Forward', 'Power Forward and Center', 'Point Guard and Small Forward and Shooting Guard',
                    'Small Forward and Power Forward and Shooting Guard', 'Small Forward and Shooting Guard and Point Guard',
                    'Center and Small Forward and Power Forward', 'Power Forward and Center and Small Forward',
                    'Small Forward and Center and Power Forward', 'Center and Power Forward and Small Forward',
                    'Shooting Guard and Power Forward and Small Forward']

position_leaf5_3 = ['Shooting Guard and Small Forward and Point Guard', 'Point Guard and Shooting Guard',
                    'Small Forward and Shooting Guard', 'Small Forward and Shooting Guard and Power Forward',
                    'Small Forward and Power Forward and Center', 'Shooting Guard and Power Forward',
                    'Power Forward and Small Forward', 'Shooting Guard and Point Guard',
                    'Shooting Guard and Small Forward', 'Shooting Guard and Small Forward and Power Forward',
                    'Center and Power Forward', 'Power Forward and Center',
                    'Point Guard and Small Forward and Shooting Guard', 'Small Forward and Power Forward and Shooting Guard',
                    'Small Forward and Shooting Guard and Point Guard', 'Center and Small Forward and Power Forward',
                    'Power Forward and Center and Small Forward', 'Small Forward and Center and Power Forward',
                    'Center and Power Forward and Small Forward', 'Shooting Guard and Power Forward and Small Forward']

position_leaf5_4 = ['Center and Power Forward', 'Power Forward and Center',
                    'Point Guard and Small Forward and Shooting Guard', 'Small Forward and Power Forward and Shooting Guard',
                    'Small Forward and Shooting Guard and Point Guard', 'Center and Small Forward and Power Forward',
                    'Power Forward and Center and Small Forward', 'Small Forward and Center and Power Forward',
                    'Center and Power Forward and Small Forward', 'Shooting Guard and Power Forward and Small Forward']


with open('Downloads/NBA_all_datasets_norm.csv', 'rb') as csvfile, open('Desktop/NBA_norm_all_output.csv', 'wb') as output:
    d_reader = csv.DictReader(csvfile)
    
    for row in d_reader:
         if row['position'] not in position_list_1 and float(row['age']) <= 0.685 and row['position'] not in position_list_2 and float(row['draft_blk']) <= 0.128:
            leafnode.append(1)
            pred_per_val = -0.0402 * float(row['age']) + 22.7845 * float(row['draft_g']) - 0.1901 * float(row['fga']) + 2.2479 * float(row['draft_ft']) - 1.8953 * float(row['fta']) + 0.2071 * float(row['draft_trb']) + 73.305 * float(row['draft_blk']) + 0.8181 * float(row['draft_tov']) - 0.0491 * float(row['draft_pf']) + 1.9045 * float(row['fg_per']) - 0.1403 * float(row['ft_per']) + 0.312 * float(row['pts_per']) + 25.9167 * float(row['trb_per']) + 0.1053 * float(row['ast_per']) - 1.7437 * float(row['height']) + 0.0422 * float(row['amature_honor']) - 55.5555                                
            if row['position'] in position_leaf1_1:
                pred_per_val += 10.9537
            if row['position'] in position_leaf1_2:
                pred_per_val += 0.0518 
            if row['position'] in position_leaf1_3:
                pred_per_val += 0.0692
            pred_per.append(pred_per_val)
        
         if row['position'] not in position_list_1 and float(row['age']) <= 0.685 and row['position'] not in position_list_2 and float(row['draft_blk']) > 0.128:
            leafnode.append(2)
            pred_per_val = 0.0402 * float(row['age']) + 22.7845 * float(row['draft_g']) - 0.1901 * float(row['fga']) + 2.2479 * float(row['draft_ft']) - 1.8953 * float(row['fta']) + 0.2071 * float(row['draft_trb']) + 51.5546 * float(row['draft_blk']) + 0.8181 * float(row['draft_tov']) - 0.0491 * float(row['draft_pf']) + 1.9045 * float(row['fg_per']) - 0.1403 * float(row['ft_per']) + 0.312 * float(row['pts_per']) + 25.9167 * float(row['trb_per']) + 0.1053 * float(row['ast_per']) - 1.7437 * float(row['height']) + 0.0422 * float(row['amature_honor']) - 45.6398                           
            if row['position'] in position_leaf2_1:
                pred_per_val += 10.9537
            if row['position'] in position_leaf2_2:
                pred_per_val += 0.0518
            if row['position'] in position_leaf2_3:
                pred_per_val += 0.0692
            pred_per.append(pred_per_val)
            
         if row['position'] not in position_list_1 and float(row['age']) <= 0.685 and row['position'] in position_list_2:
            leafnode.append(3)
            pred_per_val = -0.0402 * float(row['age']) + 10.2187 * float(row['draft_g']) - 0.1901 * float(row['fga']) + 2.2479 * float(row['draft_ft']) - 1.8953 * float(row['fta']) + 0.2071 * float(row['draft_trb']) + 1.5288 * float(row['draft_blk']) + 0.8181 * float(row['draft_tov']) - 0.0491 * float(row['draft_pf']) + 1.9045 * float(row['fg_per']) - 0.1403 * float(row['ft_per']) + 0.312 * float(row['pts_per']) + 11.5498 * float(row['trb_per']) + 0.1053 * float(row['ast_per']) - 1.7437 * float(row['height']) + 0.0422 * float(row['amature_honor']) - 11.3002
            if row['position'] in position_leaf3_1:
                pred_per_val += 6.9498
            if row['position'] in position_leaf3_2:
                pred_per_val += 0.0518 
            if row['position'] in position_leaf3_3:
                pred_per_val += 0.0422
            pred_per.append(pred_per_val)
        
         if row['position'] not in position_list_1 and float(row['age']) > 0.685:
            leafnode.append(4)
            pred_per_val = -34.3579 * float(row['age']) + 12.8876 * float(row['draft_g']) - 0.1901 * float(row['fga']) + 19.5791 * float(row['draft_ft']) - 18.6315 * float(row['fta']) + 0.2071 * float(row['draft_trb']) + 9.5098 * float(row['draft_blk']) + 0.3609 * float(row['draft_tov']) - 0.0491 * float(row['draft_pf']) - 11.2477 * float(row['draft_pts']) + 8.2531 * float(row['fg_per']) - 0.1403 * float(row['ft_per']) + 5.0846 * float(row['mp_per']) + 17.9108 * float(row['pts_per']) + 0.1053 * float(row['ast_per']) - 0.8096 * float(row['height']) + 0.0422 * float(row['amature_honor']) + 12.7189
            if row['position'] in position_leaf4_1:
                pred_per_val += 1.9217
            if row['position'] in position_leaf4_2:
                pred_per_val += 0.0518
            if row['position'] in position_leaf4_3:
                pred_per_val += 0.0692  
            pred_per.append(pred_per_val)
            
         if row['position'] in position_list_1:
            leafnode.append(5)
            pred_per_val = -2.3994 * float(row['age']) - 6.5469 * float(row['draft_g']) + 4.2706 * float(row['mp'])  - 3.8959 * float(row['fga']) + 10.5693 * float(row['draft_ft']) - 10.6978 * float(row['fta']) + 10.0498 * float(row['draft_trb']) + 5.6632 * float(row['draft_ast']) + 3.8921 * float(row['draft_stl']) + 2.4066 * float(row['draft_blk']) + 0.0393 * float(row['draft_tov']) - 0.0203 * float(row['draft_pf']) + 2.9218 * float(row['draft_pts']) + 4.2219 * float(row['fg_per']) - 5.3306 * float(row['ft_per']) - 4.908 * float(row['mp_per'])+ 4.0119 * float(row['pts_per']) - 4.9526 * float(row['trb_per']) + 0.0435 * float(row['ast_per']) - 0.1102 * float(row['height']) + 1.0254 * float(row['amature_honor']) + 13.6087
            if row['position'] in position_leaf5_1:
                pred_per_val += 0.3595
            if row['position'] in position_leaf5_2:
                pred_per_val += 0.8272 
            if row['position'] in position_leaf5_3:
                pred_per_val += 0.53
            if row['position'] in position_leaf5_4:
                pred_per_val += 1.3406
            pred_per.append(pred_per_val) 
            
with open('Downloads/NBA_all_datasets_norm.csv', 'rb') as input, open('Documents/NBA_norm_all_output.csv', 'wb') as output:
    reader = csv.reader(input, delimiter = ',')
    writer = csv.writer(output, delimiter = ',')
    
    row = next(reader)  # read title line
    row.append('LeafNode')
    row.append('pred_per')
    writer.writerow(row)
    
    it_leafNode = leafnode.__iter__()  # create an iterator on the result
    it_pred_per = pred_per.__iter__()
    
    for row in reader:
        if row:  # avoid empty lines that usually lurk undetected at the end of the files
            try:
                row.append(next(it_leafNode))  # add a result to current row
                row.append(next(it_pred_per))
            except StopIteration:
                row.append("N/A")     # not enough results: pad with N/A
            writer.writerow(row)