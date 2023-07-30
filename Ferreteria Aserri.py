from tkinter import *
import random
import os
import sys
from tkinter import messagebox
raiz = Tk()

class MenuFactura:
    def __init__(kev, raiz):
        kev.raiz = raiz
        kev.raiz.geometry("1350x700+0+0")
        kev.raiz.configure(bg="skyblue")
        kev.raiz.title("Ferreteria Aserri")
        titulo = Label(kev.raiz, text="✤Ferreteria Aserri✤", bd=10, relief=GROOVE, font=(
            "Arial Black", 40), bg="cyan", fg="black").pack(fill=X)
        # ===================================variables=======================================================================================
        kev.MartilloEncofrador = IntVar()
        kev.MartilloChapista = IntVar()
        kev.MazaGoma = IntVar()
        kev.PalaPunta = IntVar()
        kev.PalaCuadrada = IntVar()
        kev.Cortarremaches = IntVar()
        kev.TenazasCarpintero = IntVar()
        kev.BrochaPintor = IntVar()
        kev.Rodillo = IntVar()
        kev.Aguarrás = IntVar()
        kev.DisolventeNitro = IntVar()
        kev.DisolventeUniversal = IntVar()
        kev.PistolaPintar = IntVar()
        kev.RodilloEspuma = IntVar()
        kev.LlaveFija = IntVar()
        kev.LlaveAcodada = IntVar()
        kev.LlaveCombinada  = IntVar()
        kev.LlaveTubo = IntVar()
        kev.LlaveCruz = IntVar()
        kev.LlaveAllen = IntVar()
        kev.Desatornillador = IntVar()
        kev.total_v1 = StringVar()
        kev.total_v2 = StringVar()
        kev.total_v3 = StringVar()
        kev.a = StringVar()
        kev.b = StringVar()          
        kev.c = StringVar()
        kev.c_name = StringVar()
        kev.fact_no = StringVar()
        x = random.randint(1000, 9999)
        kev.fact_no.set(str(x))
        kev.cedula =StringVar()

        # ==========================================Detalles del LabelFrame del Cliente=================================================
        detalle = LabelFrame(kev.raiz, text="Datos del Cliente", font=("Arial Black", 12), bg="cyan", fg="black", relief=SUNKEN, bd=20)
        detalle.place(x=0, y=80, relwidth=1)
        nombreCliente = Label(detalle, text="Nombre:", font=("Arial Black", 14), bg="darkcyan", fg="lightcyan").grid(row=0, column=0, padx=15)
        cliente_entry = Entry(detalle, borderwidth=4, width=30,textvariable=kev.c_name,bg="lightcyan").grid(row=0, column=1, padx=8)
        cedula = Label(detalle, text="Cédula:", font=("Arial Black", 14), bg="darkcyan", fg="lightcyan").grid(row=0, column=2, padx=10)
        cedula_entry = Entry(detalle, borderwidth=4, width=30,textvariable=kev.cedula,bg="lightcyan").grid(row=0, column=3, padx=8)
        factura = Label(detalle, text="Factura #", font=("Arial Black", 14), bg="darkcyan", fg="lightcyan").grid(row=0, column=4, padx=10)
        factura_entry = Entry(detalle, borderwidth=4, width=30,textvariable=kev.fact_no,bg="lightcyan").grid(row=0, column=5, padx=8)

        # =======================================Detalles del LabelFrame de Construccion=================================================================
        varios1 = LabelFrame(kev.raiz, text="Construccion", font=("Arial Black", 12), bg="cyan", fg="black", relief=GROOVE, bd=10)
        varios1.place(x=677, y=180, height=380, width=325)

                        


        
        item1 = Label(varios1, text="MartilloEncofrador", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=0, column=0, pady=11)
        item1_entry = Entry(varios1, borderwidth=2, width=15,textvariable=kev.MartilloEncofrador,bg="lightcyan").grid(row=0, column=1, padx=10)
        item2 = Label(varios1, text="MartilloChapista", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=1, column=0, pady=11)
        item2_entry = Entry(varios1, borderwidth=2, width=15,textvariable=kev.MartilloChapista,bg="lightcyan").grid(row=1, column=1, padx=10)
        item3 = Label(varios1, text="Maza de Goma", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=2, column=0, pady=11)
        item3_entry = Entry(varios1, borderwidth=2, width=15,textvariable=kev.MazaGoma,bg="lightcyan").grid(row=2, column=1, padx=10)
        item4 = Label(varios1, text="PalaPunta", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=3, column=0, pady=11)
        item4_entry = Entry(varios1, borderwidth=2, width=15,textvariable=kev.PalaPunta,bg="lightcyan").grid(row=3, column=1, padx=10)
        item5 = Label(varios1, text="PalaCuadrada", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=4, column=0, pady=11)
        item5_entry = Entry(varios1, borderwidth=2, width=15,textvariable=kev.PalaCuadrada,bg="lightcyan").grid(row=4, column=1, padx=10)
        item6 = Label(varios1, text="Cortarremaches", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=5, column=0, pady=11)
        item6_entry = Entry(varios1, borderwidth=2, width=15,textvariable=kev.Cortarremaches,bg="lightcyan").grid(row=5, column=1, padx=10)
        item7 = Label(varios1, text="Tenazas de Carpintero", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=6, column=0, pady=11)
        item7_entry = Entry(varios1, borderwidth=2, width=15,textvariable=kev.TenazasCarpintero,bg="lightcyan").grid(row=6, column=1, padx=10)

        # ===================================Detalles del LabelFrame de Pintura y Complementos=====================================================================================
        varios2 = LabelFrame(kev.raiz, text="Pintura y Complementos", font=("Arial Black", 12), relief=GROOVE, bd=10, bg="cyan", fg="black")
        varios2.place(x=340, y=180, height=380, width=325)
        item8 = Label(varios2, text="Brocha de Pintor", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=0, column=0, pady=11)
        item8_entry = Entry(varios2, borderwidth=2, width=15,textvariable=kev.BrochaPintor,bg="lightcyan").grid(row=0, column=1, padx=10)
        item9 = Label(varios2, text="Rodillo", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=1, column=0, pady=11)
        item9_entry = Entry(varios2, borderwidth=2, width=15,textvariable=kev.Rodillo,bg="lightcyan").grid(row=1, column=1, padx=10)
        item10 = Label(varios2, text="Aguarrás", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=2, column=0, pady=11)
        item10_entry = Entry(varios2, borderwidth=2, width=15,textvariable=kev.Aguarrás,bg="lightcyan").grid(row=2, column=1, padx=10)
        item11 = Label(varios2, text="DisolventeNitro", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=3, column=0, pady=11)
        item11_entry = Entry(varios2, borderwidth=2, width=15,textvariable=kev.DisolventeNitro,bg="lightcyan").grid(row=3, column=1, padx=10)
        item12 = Label(varios2, text="DisolventeUniversal", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=4, column=0, pady=11)
        item12_entry = Entry(varios2, borderwidth=2, width=15,textvariable=kev.DisolventeUniversal,bg="lightcyan").grid(row=4, column=1, padx=10)
        item13 = Label(varios2, text="Pistola de Pintar", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=5, column=0, pady=11)
        item13_entry = Entry(varios2, borderwidth=2, width=15,textvariable=kev.PistolaPintar,bg="lightcyan").grid(row=5, column=1, padx=10)
        item14 = Label(varios2, text="Rodillo de Espuma", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=6, column=0, pady=11)
        item14_entry = Entry(varios2, borderwidth=2, width=15,textvariable=kev.RodilloEspuma,bg="lightcyan").grid(row=6, column=1, padx=10)

        # ========================================Detalles del LabelFrame de Industria==============================================================================
        varios3 = LabelFrame(kev.raiz, text="Industria", font=("Arial Black", 12), relief=GROOVE, bd=10, bg="cyan", fg="black")
    
        varios3.place(x=0, y=180, height=380, width=325)



        item15 = Label(varios3, text="LlaveFija", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=0, column=0, pady=11)
        item15_entry = Entry(varios3, borderwidth=2, width=15,textvariable=kev.LlaveFija,bg="lightcyan").grid(row=0, column=1, padx=10)
        item16 = Label(varios3, text="LlaveAcodada", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=1, column=0, pady=11)
        item16_entry = Entry(varios3, borderwidth=2, width=15,textvariable=kev.LlaveAcodada,bg="lightcyan").grid(row=1, column=1, padx=10)
        item17 = Label(varios3, text="LlaveCombinada", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=2, column=0, pady=11)
        item17_entry = Entry(varios3, borderwidth=2, width=15,textvariable=kev.LlaveCombinada,bg="lightcyan").grid(row=2, column=1, padx=10)
        item18 = Label(varios3, text="LlaveTubo", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=3, column=0, pady=11)
        item18_entry = Entry(varios3, borderwidth=2, width=15,textvariable=kev.LlaveTubo,bg="lightcyan").grid(row=3, column=1, padx=10)
        item19 = Label(varios3, text="LlaveCruz", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=4, column=0, pady=11)
        item19_entry = Entry(varios3, borderwidth=2, width=15,textvariable=kev.LlaveCruz,bg="lightcyan").grid(row=4, column=1, padx=10)
        item20 = Label(varios3, text="LlaveAllen", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=5, column=0, pady=11)
        item20_entry = Entry(varios3, borderwidth=2, width=15,textvariable=kev.LlaveAllen,bg="lightcyan").grid(row=5, column=1, padx=10)
        item21 = Label(varios3, text="Desatornillador", font=("Arial Black", 11), bg="darkcyan", fg="lightcyan").grid(row=6, column=0, pady=11)
        item21_entry = Entry(varios3, borderwidth=2, width=15,textvariable=kev.Desatornillador,bg="lightcyan").grid(row=6, column=1, padx=10)

        # =====================================================Facturación====================================================================================================
        facturacion = Frame(kev.raiz, bd=10, relief=GROOVE, bg="navy")
        facturacion.place(x=1010, y=188, width=330, height=372)
        factura_title = Label(facturacion, text="Área de Facturación", font=("Arial Black", 17), bd=7, relief=GROOVE, bg="cyan", fg="black").pack(fill=X)
        scrol_y = Scrollbar(facturacion, orient=VERTICAL)
        kev.txtarea = Text(facturacion, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=kev.txtarea.yview)
        kev.txtarea.pack(fill=BOTH, expand=1)
        # =================================================Detalle Facturación================================================================================================
        detalleFacturacion = LabelFrame(kev.raiz, text="Resumen de factura", font=("Arial Black", 12), relief=GROOVE, bd=10, bg="teal", fg="lightcyan")
        detalleFacturacion.place(x=0, y=560, relwidth=1, height=137)

        total_varios1 = Label(detalleFacturacion, text="Precio Total Construccion", font=("Arial Black", 11), bg="cyan", fg="black").grid(row=0, column=0)
        total_varios1_entry = Entry(detalleFacturacion, width=30, borderwidth=2,textvariable=kev.total_v1,bg="lightcyan").grid(row=0, column=1, padx=10, pady=7)
        total_varios2 = Label(detalleFacturacion, text="Precio Total Pintura y Complementos", font=("Arial Black", 11), bg="cyan", fg="black").grid(row=1, column=0)
        total_varios2_entry = Entry(detalleFacturacion, width=30, borderwidth=2,textvariable=kev.total_v2,bg="lightcyan").grid(row=1, column=1, padx=10, pady=7)
        total_varios3 = Label(detalleFacturacion, text="Precio Total Industria", font=("Arial Black", 11), bg="cyan", fg="black").grid(row=2, column=0)
        total_varios3_entry = Entry(detalleFacturacion, width=30, borderwidth=2,textvariable=kev.total_v3,bg="lightcyan").grid(row=2, column=1, padx=10, pady=7)

        tax_varios1 = Label(detalleFacturacion, text="IVA Construccion", font=("Arial Black", 11), bg="cyan", fg="black").grid(row=0, column=2)
        tax_varios1_entry = Entry(detalleFacturacion, width=30, borderwidth=2, textvariable=kev.a,bg="lightcyan").grid(row=0, column=3, padx=10, pady=7)
        tax_varios2 = Label(detalleFacturacion, text="IVA Pintura y Complementos", font=("Arial Black", 11), bg="cyan", fg="black").grid(row=1, column=2)
        tax_varios2_entry = Entry(detalleFacturacion, width=30, borderwidth=2, textvariable=kev.b,bg="lightcyan").grid(row=1, column=3, padx=10, pady=7)
        tax_varios3 = Label(detalleFacturacion, text="IVA Industria", font=("Arial Black", 11), bg="cyan", fg="black").grid(row=2, column=2)
        tax_varios3_entry = Entry(detalleFacturacion, width=30, borderwidth=2, textvariable=kev.c,bg="lightcyan").grid(row=2, column=3, padx=10, pady=7)

        botones_frame = Frame(detalleFacturacion, bd=7, relief=GROOVE, bg="darkblue")
        botones_frame.place(x=900, width=425, height=95)
        boton_total = Button(botones_frame, text="Total Facturado", font=("Arial Black", 14), pady=10,
                              bg="aquamarine", fg="darkblue", command=lambda: total(kev)).grid(row=0, column=1, padx=12)
        boton_borrar = Button(botones_frame, text="Borrar", font=("Arial Black", 14), pady=10,
                              bg="aquamarine", fg="darkblue", command=lambda: clear(kev)).grid(row=0, column=2, padx=5, pady=6)
        button_exit = Button(botones_frame, text="Salir", font=("Arial Black", 14), pady=10, bg="aquamarine",
                             fg="darkblue", width=6, command=lambda: exit1(kev)).grid(row=0, column=3, padx=5, pady=6)
        intro(kev)

def total(kev):
    if (kev.c_name.get == "" or kev.cedula.get() == ""):
        messagebox.showerror("Error", "Debe completar los datos del cliente!!!!!!!!")
    kev.nu = kev.MartilloEncofrador.get()*4000
    kev.no = kev.MartilloChapista.get()*2000
    kev.la = kev.MazaGoma.get()*5000
    kev.ore = kev.PalaPunta.get()*4500
    kev.mu = kev.PalaCuadrada.get()*7500
    kev.si = kev.Cortarremaches.get()*8750
    kev.na = kev.TenazasCarpintero.get()*1680
    total_varios1_price = (kev.nu + kev.no + kev.la + kev.ore + kev.mu + kev.si + kev.na)
    kev.total_v1.set(str(total_varios1_price)+" COLONES")
    kev.a.set(str(round(total_varios1_price*0.05, 3))+" COLONES")

    kev.at = kev.BrochaPintor.get()*2500
    kev.pa = kev.Rodillo.get()*1750
    kev.oi = kev.Aguarrás.get()*1000
    kev.ri = kev.DisolventeNitro.get()*1850
    kev.su = kev.DisolventeUniversal.get()*1550
    kev.te = kev.PistolaPintar.get()*7800
    kev.da = kev.RodilloEspuma.get()*1125
    total_varios2_price = (kev.at + kev.pa + kev.oi + kev.ri + kev.su + kev.te + kev.da)
    kev.total_v2.set(str(total_varios2_price)+" COLONES")
    kev.b.set(str(round(total_varios2_price*0.13, 3))+" COLONES")

    kev.so = kev.LlaveFija.get()*700
    kev.sh = kev.LlaveAcodada.get()*800
    kev.cr = kev.LlaveCombinada.get()*2000
    kev.lo = kev.LlaveTubo.get()*2500
    kev.fo = kev.LlaveCruz.get()*1500
    kev.ma = kev.LlaveAllen.get()*3800
    kev.sa = kev.Desatornillador.get()*1500
    total_varios3_price = (kev.so + kev.sh + kev.cr + kev.lo + kev.fo + kev.ma + kev.sa)
    kev.total_v3.set(str(total_varios3_price)+" colones")
    kev.c.set(str(round(total_varios3_price*0.13, 3))+" colones")

    kev.total_fact = (total_varios1_price + total_varios2_price + total_varios3_price + 
                           (round(total_varios2_price*0.13, 3)) +
                           (round(total_varios3_price*0.13, 3)) +
                           (round(total_varios1_price*0.13, 3)))
    kev.total_Fact_all = str(kev.total_fact)+" COLONES"
    facturacion(kev)


def intro(kev):
    kev.txtarea.delete(1.0, END)
    kev.txtarea.insert(
        END, "Bienvenid@ a la Unidad Productiva \n\t\tAserrí\n\tTeléfono +506 2230-5222")
    kev.txtarea.insert(END, f"\n\nFactura Número. : {kev.fact_no.get()}")
    kev.txtarea.insert(END, f"\nNombre Cliente : {kev.c_name.get()}")
    kev.txtarea.insert(END, f"\nTeléfono No. : {kev.cedula.get()}")
    kev.txtarea.insert(END, "\n====================================\n")
    kev.txtarea.insert(END, "\nProducto\t\tCantidad\tPrecio\n")
    kev.txtarea.insert(END, "\n====================================\n")


def facturacion(kev):
    intro(kev)
    if kev.MartilloEncofrador.get() != 0:
        kev.txtarea.insert(END, f"MartilloEncofrador\t\t {kev.MartilloEncofrador.get()}\t{kev.nu}\n")
    if kev.MartilloChapista.get() != 0:
        kev.txtarea.insert(END, f"MartilloChapista\t\t {kev.MartilloChapista.get()}\t{kev.no}\n")
    if kev.MazaGoma.get() != 0:
        kev.txtarea.insert(END, f"MazaGoma\t\t {kev.MazaGoma.get()}\t{kev.la}\n")
    if kev.PalaPunta.get() != 0:
        kev.txtarea.insert(END, f"PalaPunta\t\t {kev.PalaPunta.get()}\t{kev.ore}\n")
    if kev.PalaCuadrada.get() != 0:
        kev.txtarea.insert(END, f"PalaCuadrada\t\t {kev.PalaCuadrada.get()}\t{kev.mu}\n")
    if kev.Cortarremaches.get() != 0:
        kev.txtarea.insert(END, f"Cortarremaches\t\t {kev.Cortarremaches.get()}\t{kev.si}\n")
    if kev.TenazasCarpintero.get() != 0:
        kev.txtarea.insert(END, f"TenazasCarpintero\t\t {kev.TenazasCarpintero.get()}\t{kev.na}\n")
    if kev.BrochaPintor.get() != 0:
        kev.txtarea.insert(END, f"BrochaPintor\t\t {kev.BrochaPintor.get()}\t{kev.at}\n")
    if kev.Rodillo.get() != 0:
        kev.txtarea.insert(END, f"Rodillo\t\t {kev.Rodillo.get()}\t{kev.pa}\n")
    if kev.Aguarrás.get() != 0:
        kev.txtarea.insert(END, f"Aguarrás\t\t {kev.Aguarrás.get()}\t{kev.ri}\n")
    if kev.DisolventeNitro.get() != 0:
        kev.txtarea.insert(END, f"DisolventeNitro\t\t {kev.DisolventeNitro.get()}\t{kev.oi}\n")
    if kev.DisolventeUniversal.get() != 0:
        kev.txtarea.insert(END, f"DisolventeUniversal\t\t {kev.DisolventeUniversal.get()}\t{kev.su}\n")
    if kev.PistolaPintar.get() != 0:
        kev.txtarea.insert(END, f"PistolaPintar\t\t {kev.PistolaPintar.get()}\t{kev.da}\n")
    if kev.RodilloEspuma.get() != 0:
        kev.txtarea.insert(END, f"RodilloEspuma\t\t {kev.RodilloEspuma.get()}\t{kev.te}\n")
    if kev.LlaveFija.get() != 0:
        kev.txtarea.insert(END, f"LlaveFija\t\t {kev.LlaveFija.get()}\t{kev.so}\n")
    if kev.LlaveAcodada.get() != 0:
        kev.txtarea.insert(END, f"LlaveAcodada\t\t {kev.LlaveAcodada.get()}\t{kev.sh}\n")
    if kev.LlaveCombinada.get() != 0:
        kev.txtarea.insert(END, f"LlaveCombinada\t\t {kev.LlaveCombinada.get()}\t{kev.lo}\n")
    if kev.LlaveTubo.get() != 0:
        kev.txtarea.insert(END, f"LlaveTubo\t\t {kev.LlaveTubo.get()}\t{kev.cr}\n")
    if kev.LlaveCruz.get() != 0:
        kev.txtarea.insert(END, f"LlaveCruz\t\t {kev.LlaveCruz.get()}\t{kev.fo}\n")
    if kev.LlaveAllen.get() != 0:
        kev.txtarea.insert(END, f"LlaveAllen\t\t {kev.LlaveAllen.get()}\t{kev.ma}\n")
    if kev.Desatornillador.get() != 0:
        kev.txtarea.insert(
            END, f"Desatornillador\t\t {kev.Desatornillador.get()}\t{kev.sa}\n")

    kev.txtarea.insert(END, f"====================================\n")
    if kev.a.get() != "0.0 Colones":
        kev.txtarea.insert(END, f"Total IVA Construccion: {kev.a.get()}\n")
    if kev.b.get() != "0.0 COP":
        kev.txtarea.insert(
            END, f"Total IVA Pintura y Complementos: {kev.b.get()}\n")
    if kev.c.get() != "0.0 Colones":
        kev.txtarea.insert(END, f"Total IVA Industria: {kev.c.get()}\n")
    kev.txtarea.insert(END, f"Monto total facturado : {kev.total_Fact_all}\n")
    kev.txtarea.insert(END, f"====================================\n")

#Función que se ejecuta con el botón limpiar
def clear(kev):
    kev.txtarea.delete(1.0, END)
    kev.MartilloEncofrador.set(0)
    kev.MartilloChapista.set(0)
    kev.MazaGoma.set(0)
    kev.PalaPunta.set(0)
    kev.PalaCuadrada.set(0)
    kev.Cortarremaches.set(0)
    kev.TenazasCarpintero.set(0)
    kev.BrochaPintor.set(0)
    kev.Rodillo.set(0)
    kev.Aguarrás.set(0)
    kev.DisolventeNitro.set(0)
    kev.DisolventeUniversal.set(0)
    kev.PistolaPintar.set(0)
    kev.RodilloEspuma.set(0)
    kev.LlaveFija.set(0)
    kev.LlaveAcodada.set(0)
    kev.LlaveCombinada.set(0)
    kev.LlaveTubo.set(0)
    kev.LlaveCruz.set(0)
    kev.LlaveAllen.set(0)
    kev.Desatornillador.set(0)
    kev.total_v1.set(0)
    kev.total_v2.set(0)
    kev.total_v3.set(0)
    kev.a.set(0)
    kev.b.set(0)
    kev.c.set(0)
    kev.c_name.set(0)
    kev.fact_no.set(0)
    kev.fact_no.set(0)
    kev.cedula.set(0)


def exit1(kev):
    kev.raiz.destroy()

obj = MenuFactura(raiz)
raiz.mainloop()
