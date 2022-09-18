import treatment as trmt

def main():
    pat = trmt.patient()
    procedure_list = trmt.proc_list()
    trmt.display_list(procedure_list, pat)

if __name__ == '__main__': main()