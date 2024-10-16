title='Program Bantuan Sosial Bahan Pangan'
print(title.upper())
biodata1="Cipto"
pekerjaan='Pedagang Buah'
umur= 51
status='duda'
gaji=1200000.00
# print(f'Nama:{biodata1}')
# print(f'Nama Pekerjaan:{pekerjaan}')
# print(f'status kawin:{status}')
# print(f'gaji:Rp.{gaji}')

biodata2='Ahmad'
pekerjaannya='Ojek Online'
umur=34
statusnya='Belum menikah'
gajinya=1000000.00
# print(f'Nama:{biodata2}')
# print(f'Nama Pekerjaan:{pekerjaannya}')
# print(f'status kawin:{statusnya}')
# print(f'gaji:Rp.{gajinya}')

biodata3='Carmad'
pekerjaandia='purna tni'
umurdia= 59
statusdia='Menikah'
gajidia=1400000.00
# print(f'Nama:{biodata3}')
# print(f'Nama Pekerjaan:{pekerjaandia}')
# print(f'status kawin:{statusdia}')
# print(f'gaji:Rp.{gajidia}')


nama_pekerjaan=['tni','polisi','pns','dokter','purna tni','purna pns','purna polisi','purna dokter','purna pns']

nama1=input('Masukan Nama Warga:')
pekerjaan1=input('Masuka Nama Pekerjaan:')
gaji1=float(input('Masukan Gaji:Rp.'))
status=input('Masukan status warga:')
umur1=int(input('Masukan umur warga:'))

if(umur1 > 50 and gaji1 <= 1500000 and pekerjaan1 not in nama_pekerjaan):
    hasil1=('Memenuhi Syarat Bansos')
else:
    hasil1=('Tidak Memenuhi Syarat Bansos')

nama2=input('Masukan Nama Warga yang kedua:')
pekerjaan2=input('Masukan Nama Pekerjaan:')
gaji2=float(input('Masukan Nominal gaji:Rp.'))
status2=input('Masukan status warga:')
umur2=int(input('Masukan umur warga:'))

if(umur2 > 45 and gaji2 <= 1500000 and pekerjaan2 not in nama_pekerjaan):
    hasil2=('Memenuhi Syarat Bansos')
else:
    hasil2=('Tidak Memenuhi Syarat Bansos')

nama3=input('Masukan Nama Warga yang ketiga:')
pekerjaan3=input('Masukan Nama Pekerjaan:')
gaji3=float(input('Masukan Nominal gaji:Rp.'))
status3=input('Masukan status warga:')
umur3=int(input('Masukan umur warga:'))

if(umur3 > 50 and gaji3 <= 1500000 and pekerjaan3 not in nama_pekerjaan):
    hasil3=('Memenuhi Syarat Bansos')
else:
    hasil3=('Tidak Memenuhi Syarat Bansos')



print('Nama Warga yang Pertama:',nama1)
print('Umur:',umur1)
print('Nominal Gaji:Rp.',gaji1)
print('Nama pekerjaannya:',pekerjaan1)
print(hasil1)
print('Nama Warga yang Kedua:',nama2)
print('Umur:',umur2)
print('Nominal Gaji:Rp.',gaji2)
print('Nama Pekerjaannya:',pekerjaan2)
print(hasil2)
print('Nama Warga yang Ketiga:',nama3)
print('Umur:',umur3)
print('Nominal Gaji:Rp.',gaji3)
print('Nama Pekerjaannya:',pekerjaan3)
print(hasil3)


