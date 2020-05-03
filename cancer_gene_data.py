import numpy as np
genes = [
        "CNS",          
        "CNS",        
        "CNS",        
        "RENAL",      
        "BREAST",    
        "CNS",       
        "CNS",       
        "BREAST",      
        "NSCLC",       
        "NSCLC",    
        "RENAL",         
        "RENAL",     
        "RENAL",       
        "RENAL",       
        "RENAL",       
        "RENAL",         
        "RENAL",        
        "BREAST", 
        "NSCLC",      
        "RENAL",       
        "UNKNOWN",    
        "OVARIAN",    
        "MELANOMA",
        "PROSTATE",   
        "OVARIAN",    
        "OVARIAN",  
        "OVARIAN",     
        "OVARIAN",    
        "OVARIAN",    
        "PROSTATE",   
        "NSCLC",        
        "NSCLC",        
        "NSCLC",     
        "LEUKEMIA",
        "K562B-repro",               
        "K562A-repro",               
        "LEUKEMIA",   
        "LEUKEMIA",  
        "LEUKEMIA",    
        "LEUKEMIA",  
        "LEUKEMIA",       
        "COLON",      
        "COLON",       
        "COLON",      
        "COLON",        
        "COLON",     
        "COLON",      
        "COLON",     
        "MCF7A-repro",               
        "BREAST",       
        "MCF7D-repro",               
        "BREAST",     
        "NSCLC",     
        "NSCLC",     
        "NSCLC",    
        "MELANOMA", 
        "BREAST", 
        "BREAST",      
        "MELANOMA",     
        "MELANOMA",
        "MELANOMA",  
        "MELANOMA", 
        "MELANOMA",  
        "MELANOMA", 
        ]

def read_data():
    gene_data = [[] for l in genes]
    with open('nci_data.data') as f:
        for line in f:
            li = filter( lambda x: '' is not x ,line.split(' '))
            [ gene_data[a].append(float(b)) for a,b in enumerate(li)]
    data = np.array(gene_data)
    return genes,data

if __name__ == '__main__':
    genes, data = read_data()
    import pdb; pdb.set_trace()  # breakpoint bbc91d71 //
    print('done')