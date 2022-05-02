import nibabel as nb

data_dir = 'MRIsamples/'
data_dir_save = data_dir + 'hdr_to_nii/'
data_ext = '.hdr'
data_ext_save = '.nii'
filenames = ['4_8', '8_4', '100_23', '205_3']

for filename in filenames:
    try:
        #Se carga la imagen MRI simple
        path = data_dir + filename + data_ext
        img = nb.load(path)

        #Se muestra la información del encabezado
        print(img.header)
        print('*********************************************************************')

        #Se guarda la imagen MRI en formao NIFTI
        path = path.replace(data_dir, data_dir_save).replace(data_ext, data_ext_save)
        nb.save(img, path)
    except FileNotFoundError:
        print(f"No se pudo cargar el archivo: '{filename + data_ext}'")
        print('*********************************************************************')
    except AttributeError:
        print(f"El archivo: '{filename + data_ext}', se encuentra vacio")
        print('*********************************************************************')

