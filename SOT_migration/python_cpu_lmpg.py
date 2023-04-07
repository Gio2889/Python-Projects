with open(path, 'rb') as f:
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b'\n':
                f.seek(-2, os.SEEK_CUR)
            last_line = f.readline().decode()
            cputime=last_line.split()[2]
            if cputime.find('m')==-1:
                cputime=float(cputime.split('s')[0])/60
            elif cputime.find('s')==-1:
                cputime=float(cputime.split('m')[0])
        print(cputime)
