from header import *

def R_mp2(ph, ps, ch, h1, h2, h3):
    s9 = R_ax_mp(f"{ph}", f"→{ps}{ch}", h1, h3)
    return R_ax_mp(f"{ps}", f"{ch}", h2, s9)

def R_mp2b(ph, ps, ch, h1, h2, h3):
    s6 = R_ax_mp(f"{ph}", f"{ps}", h1, h2)
    return R_ax_mp(f"{ps}", f"{ch}", s6, h3)

def R_a1i(ph, ps, h1):
    s7 = R_ax_1(f"{ph}", f"{ps}")
    return R_ax_mp(f"{ph}", f"→{ps}{ph}", h1, s7)

def R_2a1i(ph, ps, ch, h1):
    s7 = R_a1i(f"{ph}", f"{ch}", h1)
    return R_a1i(f"→{ch}{ph}", f"{ps}", s7)

def R_mp1i(ph, ps, ch, h1, h2):
    s6 = R_ax_mp(f"{ph}", f"{ps}", h1, h2)
    return R_a1i(f"{ps}", f"{ch}", s6)

def R_a2i(ph, ps, ch, h1):
    s16 = R_ax_2(f"{ph}", f"{ps}", f"{ch}")
    return R_ax_mp(f"→{ph}→{ps}{ch}", f"→→{ph}{ps}→{ph}{ch}", h1, s16)

def R_mpd(ph, ps, ch, h1, h2):
    s11 = R_a2i(f"{ph}", f"{ps}", f"{ch}", h2)
    return R_ax_mp(f"→{ph}{ps}", f"→{ph}{ch}", h1, s11)

def R_imim2i(ph, ps, ch, h1):
    s8 = R_a1i(f"→{ph}{ps}", f"{ch}", h1)
    return R_a2i(f"{ch}", f"{ph}", f"{ps}", s8)

def R_syl(ph, ps, ch, h1, h2):
    s9 = R_a1i(f"→{ps}{ch}", f"{ph}", h2)
    return R_mpd(f"{ph}", f"{ps}", f"{ch}", h1, s9)

def R_3syl(ph, ps, ch, th, h1, h2, h3):
    s8 = R_syl(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    return R_syl(f"{ph}", f"{ch}", f"{th}", s8, h3)

def R_4syl(ph, ps, ch, th, ta, h1, h2, h3, h4):
    s10 = R_3syl(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2, h3)
    return R_syl(f"{ph}", f"{th}", f"{ta}", s10, h4)

def R_mpi(ph, ps, ch, h1, h2):
    s6 = R_a1i(f"{ps}", f"{ph}", h1)
    return R_mpd(f"{ph}", f"{ps}", f"{ch}", s6, h2)

def R_mpisyl(ph, ps, ch, th, h1, h2, h3):
    s9 = R_mpi(f"{ps}", f"{ch}", f"{th}", h2, h3)
    return R_syl(f"{ph}", f"{ps}", f"{th}", h1, s9)

@Theorem(1, "id")
def R_id(ph):
    s8 = R_ax_1(f"{ph}", f"{ph}")
    s11 = R_ax_1(f"{ph}", f"→{ph}{ph}")
    return R_mpd(f"{ph}", f"→{ph}{ph}", f"{ph}", s8, s11)

@Theorem(2, "idd")
def R_idd(ph, ps):
    s5 = R_id(f"{ps}")
    return R_a1i(f"→{ps}{ps}", f"{ph}", s5)

def R_a1d(ph, ps, ch, h1):
    s8 = R_ax_1(f"{ps}", f"{ch}")
    return R_syl(f"{ph}", f"{ps}", f"→{ch}{ps}", h1, s8)

def R_2a1d(ph, ps, ch, th, h1):
    s9 = R_a1d(f"{ph}", f"{ps}", f"{th}", h1)
    return R_a1d(f"{ph}", f"→{th}{ps}", f"{ch}", s9)

def R_a1i13(ph, ps, ch, th, h1):
    s10 = R_a1d(f"{ps}", f"{th}", f"{ch}", h1)
    return R_a1i(f"→{ps}→{ch}{th}", f"{ph}", s10)

@Theorem(3, "2a1")
def R_2a1(ph, ps, ch):
    s5 = R_id(f"{ph}")
    return R_2a1d(f"{ph}", f"{ph}", f"{ps}", f"{ch}", s5)

def R_a2d(ph, ps, ch, th, h1):
    s17 = R_ax_2(f"{ps}", f"{ch}", f"{th}")
    return R_syl(f"{ph}", f"→{ps}→{ch}{th}", f"→→{ps}{ch}→{ps}{th}", h1, s17)

def R_sylcom(ph, ps, ch, th, h1, h2):
    s12 = R_a2i(f"{ps}", f"{ch}", f"{th}", h2)
    return R_syl(f"{ph}", f"→{ps}{ch}", f"→{ps}{th}", h1, s12)

def R_syl5com(ph, ps, ch, th, h1, h2):
    s8 = R_a1d(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_sylcom(f"{ph}", f"{ch}", f"{ps}", f"{th}", s8, h2)

def R_com12(ph, ps, ch, h1):
    s5 = R_id(f"{ps}")
    return R_syl5com(f"{ps}", f"{ps}", f"{ph}", f"{ch}", s5, h1)

def R_syl11(ph, ps, ch, th, h1, h2):
    s10 = R_syl(f"{th}", f"{ph}", f"→{ps}{ch}", h2, h1)
    return R_com12(f"{th}", f"{ps}", f"{ch}", s10)

def R_syl5(ph, ps, ch, th, h1, h2):
    s9 = R_syl5com(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2)
    return R_com12(f"{ph}", f"{ch}", f"{th}", s9)

def R_syl6(ph, ps, ch, th, h1, h2):
    s10 = R_a1i(f"→{ch}{th}", f"{ps}", h2)
    return R_sylcom(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, s10)

def R_syl56(ph, ps, ch, th, ta, h1, h2, h3):
    s11 = R_syl6(f"{ch}", f"{ps}", f"{th}", f"{ta}", h2, h3)
    return R_syl5(f"{ph}", f"{ps}", f"{ch}", f"{ta}", h1, s11)

def R_syl6com(ph, ps, ch, th, h1, h2):
    s9 = R_syl6(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2)
    return R_com12(f"{ph}", f"{ps}", f"{th}", s9)

def R_mpcom(ph, ps, ch, h1, h2):
    s8 = R_com12(f"{ph}", f"{ps}", f"{ch}", h2)
    return R_mpd(f"{ps}", f"{ph}", f"{ch}", h1, s8)

def R_syli(ph, ps, ch, th, h1, h2):
    s9 = R_com12(f"{ch}", f"{ph}", f"{th}", h2)
    return R_sylcom(f"{ps}", f"{ph}", f"{ch}", f"{th}", h1, s9)

def R_syl2im(ph, ps, ch, th, ta, h1, h2, h3):
    s12 = R_syl5(f"{ch}", f"{th}", f"{ps}", f"{ta}", h2, h3)
    return R_syl(f"{ph}", f"{ps}", f"→{ch}{ta}", h1, s12)

def R_syl2imc(ph, ps, ch, th, ta, h1, h2, h3):
    s11 = R_syl2im(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1, h2, h3)
    return R_com12(f"{ph}", f"{ch}", f"{ta}", s11)

@Theorem(2, "pm2.27")
def R_pm2_27(ph, ps):
    s7 = R_id(f"→{ph}{ps}")
    return R_com12(f"→{ph}{ps}", f"{ph}", f"{ps}", s7)

def R_mpdd(ph, ps, ch, th, h1, h2):
    s13 = R_a2d(f"{ph}", f"{ps}", f"{ch}", f"{th}", h2)
    return R_mpd(f"{ph}", f"→{ps}{ch}", f"→{ps}{th}", h1, s13)

def R_mpid(ph, ps, ch, th, h1, h2):
    s8 = R_a1d(f"{ph}", f"{ch}", f"{ps}", h1)
    return R_mpdd(f"{ph}", f"{ps}", f"{ch}", f"{th}", s8, h2)

def R_mpdi(ph, ps, ch, th, h1, h2):
    s9 = R_a1i(f"→{ps}{ch}", f"{ph}", h1)
    return R_mpdd(f"{ph}", f"{ps}", f"{ch}", f"{th}", s9, h2)

def R_mpii(ph, ps, ch, th, h1, h2):
    s7 = R_a1i(f"{ch}", f"{ps}", h1)
    return R_mpdi(f"{ph}", f"{ps}", f"{ch}", f"{th}", s7, h2)

def R_syld(ph, ps, ch, th, h1, h2):
    s11 = R_a1d(f"{ph}", f"→{ch}{th}", f"{ps}", h2)
    return R_mpdd(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, s11)

def R_syldc(ph, ps, ch, th, h1, h2):
    s9 = R_syld(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2)
    return R_com12(f"{ph}", f"{ps}", f"{th}", s9)

def R_mp2d(ph, ps, ch, th, h1, h2, h3):
    s10 = R_mpid(f"{ph}", f"{ps}", f"{ch}", f"{th}", h2, h3)
    return R_mpd(f"{ph}", f"{ps}", f"{th}", h1, s10)

def R_a1dd(ph, ps, ch, th, h1):
    s9 = R_ax_1(f"{ch}", f"{th}")
    return R_syl6(f"{ph}", f"{ps}", f"{ch}", f"→{th}{ch}", h1, s9)

def R_2a1dd(ph, ps, ch, th, ta, h1):
    s11 = R_a1dd(f"{ph}", f"{ps}", f"{ch}", f"{ta}", h1)
    return R_a1dd(f"{ph}", f"{ps}", f"→{ta}{ch}", f"{th}", s11)

def R_pm2_43i(ph, ps, h1):
    s4 = R_id(f"{ph}")
    return R_mpd(f"{ph}", f"{ph}", f"{ps}", s4, h1)

def R_pm2_43d(ph, ps, ch, h1):
    s5 = R_id(f"{ps}")
    return R_mpdi(f"{ph}", f"{ps}", f"{ps}", f"{ch}", s5, h1)

def R_pm2_43a(ph, ps, ch, h1):
    s5 = R_id(f"{ps}")
    return R_mpid(f"{ps}", f"{ph}", f"{ps}", f"{ch}", s5, h1)

def R_pm2_43b(ph, ps, ch, h1):
    s7 = R_pm2_43a(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_com12(f"{ps}", f"{ph}", f"{ch}", s7)

@Theorem(2, "pm2.43")
def R_pm2_43(ph, ps):
    s7 = R_pm2_27(f"{ph}", f"{ps}")
    return R_a2i(f"{ph}", f"→{ph}{ps}", f"{ps}", s7)

def R_imim2d(ph, ps, ch, th, h1):
    s10 = R_a1d(f"{ph}", f"→{ps}{ch}", f"{th}", h1)
    return R_a2d(f"{ph}", f"{th}", f"{ps}", f"{ch}", s10)

@Theorem(3, "imim2")
def R_imim2(ph, ps, ch):
    s8 = R_id(f"→{ph}{ps}")
    return R_imim2d(f"→{ph}{ps}", f"{ph}", f"{ps}", f"{ch}", s8)

def R_embantd(ph, ps, ch, th, h1, h2):
    s12 = R_imim2d(f"{ph}", f"{ch}", f"{th}", f"{ps}", h2)
    return R_mpid(f"{ph}", f"→{ps}{ch}", f"{ps}", f"{th}", h1, s12)

def R_3syld(ph, ps, ch, th, ta, h1, h2, h3):
    s10 = R_syld(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2)
    return R_syld(f"{ph}", f"{ps}", f"{th}", f"{ta}", s10, h3)

def R_sylsyld(ph, ps, ch, th, ta, h1, h2, h3):
    s12 = R_syl(f"{ph}", f"{ps}", f"→{th}{ta}", h1, h3)
    return R_syld(f"{ph}", f"{ch}", f"{th}", f"{ta}", h2, s12)

def R_imim12i(ph, ps, ch, th, h1, h2):
    s11 = R_imim2i(f"{ch}", f"{th}", f"{ps}", h2)
    return R_syl5(f"{ph}", f"{ps}", f"→{ps}{ch}", f"{th}", h1, s11)

def R_imim1i(ph, ps, ch, h1):
    s6 = R_id(f"{ch}")
    return R_imim12i(f"{ph}", f"{ps}", f"{ch}", f"{ch}", h1, s6)

def R_imim3i(ph, ps, ch, th, h1):
    s12 = R_imim2i(f"{ph}", f"→{ps}{ch}", f"{th}", h1)
    return R_a2d(f"→{th}{ph}", f"{th}", f"{ps}", f"{ch}", s12)

def R_sylc(ph, ps, ch, th, h1, h2, h3):
    s10 = R_syl2im(f"{ph}", f"{ps}", f"{ph}", f"{ch}", f"{th}", h1, h2, h3)
    return R_pm2_43i(f"{ph}", f"{th}", s10)

def R_syl3c(ph, ps, ch, th, ta, h1, h2, h3, h4):
    s13 = R_sylc(f"{ph}", f"{ps}", f"{ch}", f"→{th}{ta}", h1, h2, h4)
    return R_mpd(f"{ph}", f"{th}", f"{ta}", h3, s13)

def R_syl6mpi(ph, ps, ch, th, ta, h1, h2, h3):
    s10 = R_mpi(f"{ch}", f"{th}", f"{ta}", h2, h3)
    return R_syl6(f"{ph}", f"{ps}", f"{ch}", f"{ta}", h1, s10)

def R_mpsyl(ph, ps, ch, th, h1, h2, h3):
    s7 = R_a1i(f"{ph}", f"{ps}", h1)
    return R_sylc(f"{ps}", f"{ph}", f"{ch}", f"{th}", s7, h2, h3)

def R_mpsylsyld(ph, ps, ch, th, ta, h1, h2, h3):
    s8 = R_a1i(f"{ph}", f"{ps}", h1)
    return R_sylsyld(f"{ps}", f"{ph}", f"{ch}", f"{th}", f"{ta}", s8, h2, h3)

def R_syl6c(ph, ps, ch, th, ta, h1, h2, h3):
    s13 = R_syl6(f"{ph}", f"{ps}", f"{ch}", f"→{th}{ta}", h1, h3)
    return R_mpdd(f"{ph}", f"{ps}", f"{th}", f"{ta}", h2, s13)

def R_syl6ci(ph, ps, ch, th, ta, h1, h2, h3):
    s10 = R_a1d(f"{ph}", f"{th}", f"{ps}", h2)
    return R_syl6c(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1, s10, h3)

def R_syldd(ph, ps, ch, th, ta, h1, h2):
    s16 = R_imim2(f"{th}", f"{ta}", f"{ch}")
    return R_syl6c(f"{ph}", f"{ps}", f"→{th}{ta}", f"→{ch}{th}", f"→{ch}{ta}", h2, h1, s16)

def R_syl5d(ph, ps, ch, th, ta, h1, h2):
    s11 = R_a1d(f"{ph}", f"→{ps}{ch}", f"{th}", h1)
    return R_syldd(f"{ph}", f"{th}", f"{ps}", f"{ch}", f"{ta}", s11, h2)

def R_syl7(ph, ps, ch, th, ta, h1, h2):
    s10 = R_a1i(f"→{ph}{ps}", f"{ch}", h1)
    return R_syl5d(f"{ch}", f"{ph}", f"{ps}", f"{th}", f"{ta}", s10, h2)

def R_syl6d(ph, ps, ch, th, ta, h1, h2):
    s12 = R_a1d(f"{ph}", f"→{th}{ta}", f"{ps}", h2)
    return R_syldd(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1, s12)

def R_syl8(ph, ps, ch, th, ta, h1, h2):
    s11 = R_a1i(f"→{th}{ta}", f"{ph}", h2)
    return R_syl6d(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1, s11)

def R_syl9(ph, ps, ch, th, ta, h1, h2):
    s13 = R_a1i(f"→{th}→{ch}{ta}", f"{ph}", h2)
    return R_syl5d(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1, s13)

def R_syl9r(ph, ps, ch, th, ta, h1, h2):
    s12 = R_syl9(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1, h2)
    return R_com12(f"{ph}", f"{th}", f"→{ps}{ta}", s12)

def R_syl10(ph, ps, ch, th, ta, et, h1, h2, h3):
    s14 = R_syl6(f"{ph}", f"{ps}", f"{ch}", f"→{ta}{et}", h1, h3)
    return R_syldd(f"{ph}", f"{ps}", f"{th}", f"{ta}", f"{et}", h2, s14)

def R_a1ddd(ph, ps, ch, th, ta, h1):
    s10 = R_ax_1(f"{ta}", f"{th}")
    return R_syl8(f"{ph}", f"{ps}", f"{ch}", f"{ta}", f"→{th}{ta}", h1, s10)

def R_imim12d(ph, ps, ch, th, ta, h1, h2):
    s13 = R_imim2d(f"{ph}", f"{th}", f"{ta}", f"{ch}", h2)
    return R_syl5d(f"{ph}", f"{ps}", f"{ch}", f"→{ch}{th}", f"{ta}", h1, s13)

def R_imim1d(ph, ps, ch, th, h1):
    s8 = R_idd(f"{ph}", f"{th}")
    return R_imim12d(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{th}", h1, s8)

@Theorem(3, "imim1")
def R_imim1(ph, ps, ch):
    s8 = R_id(f"→{ph}{ps}")
    return R_imim1d(f"→{ph}{ps}", f"{ph}", f"{ps}", f"{ch}", s8)

@Theorem(4, "pm2.83")
def R_pm2_83(ph, ps, ch, th):
    s13 = R_imim1(f"{ps}", f"{ch}", f"{th}")
    return R_imim3i(f"→{ps}{ch}", f"→{ch}{th}", f"→{ps}{th}", f"{ph}", s13)

@Theorem(3, "peirceroll")
def R_peirceroll(ph, ps, ch):
    s21 = R_imim1(f"→{ph}{ps}", f"{ch}", f"{ph}")
    s23 = R_id(f"→→→{ph}{ps}{ph}{ph}")
    return R_syl9r(f"→→{ph}{ps}{ch}", f"→{ch}{ph}", f"→→{ph}{ps}{ph}", f"→→→{ph}{ps}{ph}{ph}", f"{ph}", s21, s23)

def R_com23(ph, ps, ch, th, h1):
    s10 = R_pm2_27(f"{ch}", f"{th}")
    return R_syl9(f"{ph}", f"{ps}", f"→{ch}{th}", f"{ch}", f"{th}", h1, s10)

def R_com3r(ph, ps, ch, th, h1):
    s10 = R_com23(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_com12(f"{ph}", f"{ch}", f"→{ps}{th}", s10)

def R_com13(ph, ps, ch, th, h1):
    s9 = R_com3r(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_com23(f"{ch}", f"{ph}", f"{ps}", f"{th}", s9)

def R_com3l(ph, ps, ch, th, h1):
    s9 = R_com3r(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_com3r(f"{ch}", f"{ph}", f"{ps}", f"{th}", s9)

@Theorem(3, "pm2.04")
def R_pm2_04(ph, ps, ch):
    s10 = R_id(f"→{ph}→{ps}{ch}")
    return R_com23(f"→{ph}→{ps}{ch}", f"{ph}", f"{ps}", f"{ch}", s10)

def R_com34(ph, ps, ch, th, ta, h1):
    s16 = R_pm2_04(f"{ch}", f"{th}", f"{ta}")
    return R_syl6(f"{ph}", f"{ps}", f"→{ch}→{th}{ta}", f"→{th}→{ch}{ta}", h1, s16)

def R_com4l(ph, ps, ch, th, ta, h1):
    s12 = R_com3l(f"{ph}", f"{ps}", f"{ch}", f"→{th}{ta}", h1)
    return R_com34(f"{ps}", f"{ch}", f"{ph}", f"{th}", f"{ta}", s12)

def R_com4t(ph, ps, ch, th, ta, h1):
    s11 = R_com4l(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1)
    return R_com4l(f"{ps}", f"{ch}", f"{th}", f"{ph}", f"{ta}", s11)

def R_com4r(ph, ps, ch, th, ta, h1):
    s11 = R_com4t(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1)
    return R_com4l(f"{ch}", f"{th}", f"{ph}", f"{ps}", f"{ta}", s11)

def R_com24(ph, ps, ch, th, ta, h1):
    s12 = R_com4t(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1)
    return R_com13(f"{ch}", f"{th}", f"{ph}", f"→{ps}{ta}", s12)

def R_com14(ph, ps, ch, th, ta, h1):
    s12 = R_com4l(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1)
    return R_com3r(f"{ps}", f"{ch}", f"{th}", f"→{ph}{ta}", s12)

def R_com45(ph, ps, ch, th, ta, et, h1):
    s17 = R_pm2_04(f"{th}", f"{ta}", f"{et}")
    return R_syl8(f"{ph}", f"{ps}", f"{ch}", f"→{th}→{ta}{et}", f"→{ta}→{th}{et}", h1, s17)

def R_com35(ph, ps, ch, th, ta, et, h1):
    s21 = R_com34(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"→{ta}{et}", h1)
    s22 = R_com45(f"{ph}", f"{ps}", f"{th}", f"{ch}", f"{ta}", f"{et}", s21)
    return R_com34(f"{ph}", f"{ps}", f"{th}", f"{ta}", f"→{ch}{et}", s22)

def R_com25(ph, ps, ch, th, ta, et, h1):
    s21 = R_com24(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"→{ta}{et}", h1)
    s22 = R_com45(f"{ph}", f"{th}", f"{ch}", f"{ps}", f"{ta}", f"{et}", s21)
    return R_com24(f"{ph}", f"{th}", f"{ch}", f"{ta}", f"→{ps}{et}", s22)

def R_com5l(ph, ps, ch, th, ta, et, h1):
    s14 = R_com4l(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"→{ta}{et}", h1)
    return R_com45(f"{ps}", f"{ch}", f"{th}", f"{ph}", f"{ta}", f"{et}", s14)

def R_com15(ph, ps, ch, th, ta, et, h1):
    s14 = R_com5l(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", f"{et}", h1)
    return R_com4r(f"{ps}", f"{ch}", f"{th}", f"{ta}", f"→{ph}{et}", s14)

def R_com52l(ph, ps, ch, th, ta, et, h1):
    s13 = R_com5l(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", f"{et}", h1)
    return R_com5l(f"{ps}", f"{ch}", f"{th}", f"{ta}", f"{ph}", f"{et}", s13)

def R_com52r(ph, ps, ch, th, ta, et, h1):
    s13 = R_com52l(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", f"{et}", h1)
    return R_com5l(f"{ch}", f"{th}", f"{ta}", f"{ph}", f"{ps}", f"{et}", s13)

def R_com5r(ph, ps, ch, th, ta, et, h1):
    s13 = R_com52l(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", f"{et}", h1)
    return R_com52l(f"{ch}", f"{th}", f"{ta}", f"{ph}", f"{ps}", f"{et}", s13)

@Theorem(4, "imim12")
def R_imim12(ph, ps, ch, th):
    s18 = R_imim2(f"{ch}", f"{th}", f"{ps}")
    s22 = R_imim1(f"{ph}", f"{ps}", f"{th}")
    return R_syl9r(f"→{ch}{th}", f"→{ps}{ch}", f"→{ps}{th}", f"→{ph}{ps}", f"→{ph}{th}", s18, s22)

@Theorem(3, "jarr")
def R_jarr(ph, ps, ch):
    s7 = R_ax_1(f"{ps}", f"{ph}")
    return R_imim1i(f"{ps}", f"→{ph}{ps}", f"{ch}", s7)

def R_jarri(ph, ps, ch, h1):
    s7 = R_ax_1(f"{ps}", f"{ph}")
    return R_syl(f"{ps}", f"→{ph}{ps}", f"{ch}", s7, h1)

def R_pm2_86d(ph, ps, ch, th, h1):
    s14 = R_ax_1(f"{ch}", f"{ps}")
    s16 = R_syl5(f"{ch}", f"→{ps}{ch}", f"{ph}", f"→{ps}{th}", s14, h1)
    return R_com23(f"{ph}", f"{ch}", f"{ps}", f"{th}", s16)

@Theorem(3, "pm2.86")
def R_pm2_86(ph, ps, ch):
    s12 = R_id(f"→→{ph}{ps}→{ph}{ch}")
    return R_pm2_86d(f"→→{ph}{ps}→{ph}{ch}", f"{ph}", f"{ps}", f"{ch}", s12)

def R_pm2_86i(ph, ps, ch, h1):
    s9 = R_jarri(f"{ph}", f"{ps}", f"→{ph}{ch}", h1)
    return R_com12(f"{ps}", f"{ph}", f"{ch}", s9)

@Theorem(2, "loolin")
def R_loolin(ph, ps):
    s13 = R_jarr(f"{ph}", f"{ps}", f"→{ps}{ph}")
    return R_pm2_43d(f"→→{ph}{ps}→{ps}{ph}", f"{ps}", f"{ph}", s13)

@Theorem(3, "loowoz")
def R_loowoz(ph, ps, ch):
    s14 = R_jarr(f"{ph}", f"{ps}", f"→{ph}{ch}")
    return R_a2d(f"→→{ph}{ps}→{ph}{ch}", f"{ps}", f"{ph}", f"{ch}", s14)

@Theorem(2, "con4")
def R_con4(ph, ps):
    return R_ax_3(f"{ph}", f"{ps}")

def R_con4i(ph, ps, h1):
    s11 = R_con4(f"{ph}", f"{ps}")
    return R_ax_mp(f"→¬{ph}¬{ps}", f"→{ps}{ph}", h1, s11)

def R_con4d(ph, ps, ch, h1):
    s12 = R_con4(f"{ps}", f"{ch}")
    return R_syl(f"{ph}", f"→¬{ps}¬{ch}", f"→{ch}{ps}", h1, s12)

def R_mt4(ph, ps, h1, h2):
    s6 = R_con4i(f"{ps}", f"{ph}", h2)
    return R_ax_mp(f"{ph}", f"{ps}", h1, s6)

def R_mt4d(ph, ps, ch, h1, h2):
    s8 = R_con4d(f"{ph}", f"{ch}", f"{ps}", h2)
    return R_mpd(f"{ph}", f"{ps}", f"{ch}", h1, s8)

def R_mt4i(ph, ps, ch, h1, h2):
    s6 = R_a1i(f"{ch}", f"{ph}", h1)
    return R_mt4d(f"{ph}", f"{ch}", f"{ps}", s6, h2)

def R_pm2_21i(ph, ps, h1):
    s7 = R_a1i(f"¬{ph}", f"¬{ps}", h1)
    return R_con4i(f"{ps}", f"{ph}", s7)

def R_pm2_24ii(ph, ps, h1, h2):
    s6 = R_pm2_21i(f"{ph}", f"{ps}", h2)
    return R_ax_mp(f"{ph}", f"{ps}", h1, s6)

def R_pm2_21d(ph, ps, ch, h1):
    s9 = R_a1d(f"{ph}", f"¬{ps}", f"¬{ch}", h1)
    return R_con4d(f"{ph}", f"{ch}", f"{ps}", s9)

@Theorem(2, "pm2.21")
def R_pm2_21(ph, ps):
    s6 = R_id(f"¬{ph}")
    return R_pm2_21d(f"¬{ph}", f"{ph}", f"{ps}", s6)

@Theorem(2, "pm2.24")
def R_pm2_24(ph, ps):
    s6 = R_pm2_21(f"{ph}", f"{ps}")
    return R_com12(f"¬{ph}", f"{ph}", f"{ps}", s6)

@Theorem(3, "jarl")
def R_jarl(ph, ps, ch):
    s8 = R_pm2_21(f"{ph}", f"{ps}")
    return R_imim1i(f"¬{ph}", f"→{ph}{ps}", f"{ch}", s8)

def R_jarli(ph, ps, ch, h1):
    s8 = R_pm2_21(f"{ph}", f"{ps}")
    return R_syl(f"¬{ph}", f"→{ph}{ps}", f"{ch}", s8, h1)

def R_pm2_18d(ph, ps, h1):
    s4 = R_id(f"{ph}")
    s15 = R_pm2_21(f"{ps}", f"¬{ph}")
    s16 = R_sylcom(f"{ph}", f"¬{ps}", f"{ps}", f"¬{ph}", h1, s15)
    return R_mt4d(f"{ph}", f"{ph}", f"{ps}", s4, s16)

@Theorem(1, "pm2.18")
def R_pm2_18(ph):
    s7 = R_id(f"→¬{ph}{ph}")
    return R_pm2_18d(f"→¬{ph}{ph}", f"{ph}", s7)

def R_pm2_18i(ph, h1):
    s7 = R_pm2_18(f"{ph}")
    return R_ax_mp(f"→¬{ph}{ph}", f"{ph}", h1, s7)

@Theorem(1, "notnotr")
def R_notnotr(ph):
    s5 = R_pm2_18(f"{ph}")
    return R_jarli(f"¬{ph}", f"{ph}", f"{ph}", s5)

def R_notnotri(ph, h1):
    s11 = R_pm2_21i(f"¬{ph}", f"¬¬¬{ph}", h1)
    return R_mt4(f"¬¬{ph}", f"{ph}", h1, s11)

def R_notnotrd(ph, ps, h1):
    s7 = R_notnotr(f"{ps}")
    return R_syl(f"{ph}", f"¬¬{ps}", f"{ps}", h1, s7)

def R_con2d(ph, ps, ch, h1):
    s12 = R_notnotr(f"{ps}")
    s14 = R_syl5(f"¬¬{ps}", f"{ps}", f"{ph}", f"¬{ch}", s12, h1)
    return R_con4d(f"{ph}", f"¬{ps}", f"{ch}", s14)

@Theorem(2, "con2")
def R_con2(ph, ps):
    s8 = R_id(f"→{ph}¬{ps}")
    return R_con2d(f"→{ph}¬{ps}", f"{ph}", f"{ps}", s8)

def R_mt2d(ph, ps, ch, h1, h2):
    s9 = R_con2d(f"{ph}", f"{ps}", f"{ch}", h2)
    return R_mpd(f"{ph}", f"{ch}", f"¬{ps}", h1, s9)

def R_mt2i(ph, ps, ch, h1, h2):
    s6 = R_a1i(f"{ch}", f"{ph}", h1)
    return R_mt2d(f"{ph}", f"{ps}", f"{ch}", s6, h2)

def R_nsyl3(ph, ps, ch, h1, h2):
    s10 = R_a1i(f"→{ph}¬{ps}", f"{ch}", h1)
    return R_mt2d(f"{ch}", f"{ph}", f"{ps}", h2, s10)

def R_con2i(ph, ps, h1):
    s5 = R_id(f"{ps}")
    return R_nsyl3(f"{ph}", f"{ps}", f"{ps}", h1, s5)

def R_nsyl(ph, ps, ch, h1, h2):
    s7 = R_nsyl3(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    return R_con2i(f"{ch}", f"{ph}", s7)

def R_nsyl2(ph, ps, ch, h1, h2):
    s8 = R_nsyl3(f"{ph}", f"{ps}", f"¬{ch}", h1, h2)
    return R_con4i(f"{ch}", f"{ph}", s8)

@Theorem(1, "notnot")
def R_notnot(ph):
    s5 = R_id(f"¬{ph}")
    return R_con2i(f"¬{ph}", f"{ph}", s5)

def R_notnoti(ph, h1):
    s6 = R_notnot(f"{ph}")
    return R_ax_mp(f"{ph}", f"¬¬{ph}", h1, s6)

def R_notnotd(ph, ps, h1):
    s7 = R_notnot(f"{ps}")
    return R_syl(f"{ph}", f"{ps}", f"¬¬{ps}", h1, s7)

def R_con1d(ph, ps, ch, h1):
    s13 = R_notnot(f"{ch}")
    s14 = R_syl6(f"{ph}", f"¬{ps}", f"{ch}", f"¬¬{ch}", h1, s13)
    return R_con4d(f"{ph}", f"{ps}", f"¬{ch}", s14)

@Theorem(2, "con1")
def R_con1(ph, ps):
    s8 = R_id(f"→¬{ph}{ps}")
    return R_con1d(f"→¬{ph}{ps}", f"{ph}", f"{ps}", s8)

def R_con1i(ph, ps, h1):
    s6 = R_id(f"¬{ps}")
    return R_nsyl2(f"¬{ps}", f"{ps}", f"{ph}", s6, h1)

def R_mt3d(ph, ps, ch, h1, h2):
    s9 = R_con1d(f"{ph}", f"{ps}", f"{ch}", h2)
    return R_mpd(f"{ph}", f"¬{ch}", f"{ps}", h1, s9)

def R_mt3i(ph, ps, ch, h1, h2):
    s7 = R_a1i(f"¬{ch}", f"{ph}", h1)
    return R_mt3d(f"{ph}", f"{ps}", f"{ch}", s7, h2)

def R_pm2_24i(ph, ps, h1):
    s6 = R_a1i(f"{ph}", f"¬{ps}", h1)
    return R_con1i(f"{ps}", f"{ph}", s6)

def R_pm2_24d(ph, ps, ch, h1):
    s8 = R_a1d(f"{ph}", f"{ps}", f"¬{ch}", h1)
    return R_con1d(f"{ph}", f"{ch}", f"{ps}", s8)

def R_con3d(ph, ps, ch, h1):
    s11 = R_notnotr(f"{ps}")
    s13 = R_syl5(f"¬¬{ps}", f"{ps}", f"{ph}", f"{ch}", s11, h1)
    return R_con1d(f"{ph}", f"¬{ps}", f"{ch}", s13)

@Theorem(2, "con3")
def R_con3(ph, ps):
    s7 = R_id(f"→{ph}{ps}")
    return R_con3d(f"→{ph}{ps}", f"{ph}", f"{ps}", s7)

def R_con3i(ph, ps, h1):
    s6 = R_id(f"¬{ps}")
    return R_nsyl(f"¬{ps}", f"{ps}", f"{ph}", s6, h1)

def R_con3rr3(ph, ps, ch, h1):
    s9 = R_con3d(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_com12(f"{ph}", f"¬{ch}", f"¬{ps}", s9)

def R_nsyld(ph, ps, ch, th, h1, h2):
    s11 = R_con3d(f"{ph}", f"{th}", f"{ch}", h2)
    return R_syld(f"{ph}", f"{ps}", f"¬{ch}", f"¬{th}", h1, s11)

def R_nsyli(ph, ps, ch, th, h1, h2):
    s11 = R_con3d(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_syl5(f"{th}", f"¬{ch}", f"{ph}", f"¬{ps}", h2, s11)

def R_nsyl4(ph, ps, ch, h1, h2):
    s7 = R_con1i(f"{ph}", f"{ch}", h2)
    return R_syl(f"¬{ch}", f"{ph}", f"{ps}", s7, h1)

def R_nsyl5(ph, ps, ch, h1, h2):
    s7 = R_nsyl4(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    return R_con1i(f"{ch}", f"{ps}", s7)

@Theorem(2, "pm3.2im")
def R_pm3_2im(ph, ps):
    s9 = R_pm2_27(f"{ph}", f"¬{ps}")
    return R_con2d(f"{ph}", f"→{ph}¬{ps}", f"{ps}", s9)

def R_jc(ph, ps, ch, h1, h2):
    s12 = R_pm3_2im(f"{ps}", f"{ch}")
    return R_sylc(f"{ph}", f"{ps}", f"{ch}", f"¬→{ps}¬{ch}", h1, h2, s12)

@Theorem(2, "jcn")
def R_jcn(ph, ps):
    s7 = R_pm2_27(f"{ph}", f"{ps}")
    return R_con3d(f"{ph}", f"→{ph}{ps}", f"{ps}", s7)

def R_jcnd(ph, ps, ch, h1, h2):
    s12 = R_jcn(f"{ps}", f"{ch}")
    return R_sylc(f"{ph}", f"{ps}", f"¬{ch}", f"¬→{ps}{ch}", h1, h2, s12)

def R_impi(ph, ps, ch, h1):
    s9 = R_con3rr3(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_con1i(f"{ch}", f"→{ph}¬{ps}", s9)

def R_expi(ph, ps, ch, h1):
    s10 = R_pm3_2im(f"{ph}", f"{ps}")
    return R_syl6(f"{ph}", f"{ps}", f"¬→{ph}¬{ps}", f"{ch}", s10, h1)

@Theorem(2, "simprim")
def R_simprim(ph, ps):
    s5 = R_idd(f"{ph}", f"{ps}")
    return R_impi(f"{ph}", f"{ps}", f"{ps}", s5)

@Theorem(2, "simplim")
def R_simplim(ph, ps):
    s6 = R_pm2_21(f"{ph}", f"{ps}")
    return R_con1i(f"{ph}", f"→{ph}{ps}", s6)

@Theorem(3, "pm2.5g")
def R_pm2_5g(ph, ps, ch):
    s8 = R_simplim(f"{ph}", f"{ps}")
    return R_pm2_24d(f"¬→{ph}{ps}", f"{ph}", f"{ch}", s8)

@Theorem(2, "pm2.5")
def R_pm2_5(ph, ps):
    return R_pm2_5g(f"{ph}", f"{ps}", f"{ps}")

@Theorem(2, "conax1")
def R_conax1(ph, ps):
    s6 = R_ax_1(f"{ps}", f"{ph}")
    return R_con3i(f"{ps}", f"→{ph}{ps}", s6)

@Theorem(3, "conax1k")
def R_conax1k(ph, ps, ch):
    s9 = R_conax1(f"{ph}", f"{ps}")
    return R_a1d(f"¬→{ph}{ps}", f"¬{ps}", f"{ch}", s9)

@Theorem(2, "pm2.51")
def R_pm2_51(ph, ps):
    return R_conax1k(f"{ph}", f"{ps}", f"{ph}")

@Theorem(2, "pm2.52")
def R_pm2_52(ph, ps):
    return R_conax1k(f"{ph}", f"{ps}", f"¬{ph}")

@Theorem(3, "pm2.521g")
def R_pm2_521g(ph, ps, ch):
    s8 = R_conax1(f"{ph}", f"{ps}")
    return R_pm2_21d(f"¬→{ph}{ps}", f"{ps}", f"{ch}", s8)

@Theorem(3, "pm2.521g2")
def R_pm2_521g2(ph, ps, ch):
    s8 = R_simplim(f"{ph}", f"{ps}")
    return R_a1d(f"¬→{ph}{ps}", f"{ph}", f"{ch}", s8)

@Theorem(2, "pm2.521")
def R_pm2_521(ph, ps):
    return R_pm2_521g(f"{ph}", f"{ps}", f"{ph}")

@Theorem(3, "expt")
def R_expt(ph, ps, ch):
    s18 = R_pm3_2im(f"{ph}", f"{ps}")
    s19 = R_imim1d(f"{ph}", f"{ps}", f"¬→{ph}¬{ps}", f"{ch}", s18)
    return R_com12(f"{ph}", f"→¬→{ph}¬{ps}{ch}", f"→{ps}{ch}", s19)

@Theorem(3, "impt")
def R_impt(ph, ps, ch):
    s17 = R_simprim(f"{ph}", f"{ps}")
    s23 = R_simplim(f"{ph}", f"¬{ps}")
    s24 = R_imim1i(f"¬→{ph}¬{ps}", f"{ph}", f"→{ps}{ch}", s23)
    return R_mpdi(f"→{ph}→{ps}{ch}", f"¬→{ph}¬{ps}", f"{ps}", f"{ch}", s17, s24)

def R_pm2_61d(ph, ps, ch, h1, h2):
    s11 = R_con1d(f"{ph}", f"{ps}", f"{ch}", h2)
    s13 = R_syld(f"{ph}", f"¬{ch}", f"{ps}", f"{ch}", s11, h1)
    return R_pm2_18d(f"{ph}", f"{ch}", s13)

def R_pm2_61d1(ph, ps, ch, h1, h2):
    s10 = R_a1i(f"→¬{ps}{ch}", f"{ph}", h2)
    return R_pm2_61d(f"{ph}", f"{ps}", f"{ch}", h1, s10)

def R_pm2_61d2(ph, ps, ch, h1, h2):
    s8 = R_a1i(f"→{ps}{ch}", f"{ph}", h2)
    return R_pm2_61d(f"{ph}", f"{ps}", f"{ch}", s8, h1)

def R_pm2_61i(ph, ps, h1, h2):
    s6 = R_nsyl4(f"{ph}", f"{ps}", f"{ps}", h1, h2)
    return R_pm2_18i(f"{ps}", s6)

def R_pm2_61ii(ph, ps, ch, h1, h2, h3):
    s9 = R_pm2_61d2(f"¬{ph}", f"{ps}", f"{ch}", h1, h3)
    return R_pm2_61i(f"{ph}", f"{ch}", h2, s9)

def R_pm2_61nii(ph, ps, ch, h1, h2, h3):
    s7 = R_pm2_61d1(f"{ph}", f"{ps}", f"{ch}", h1, h3)
    return R_pm2_61i(f"{ph}", f"{ch}", s7, h2)

def R_pm2_61iii(ph, ps, ch, th, h1, h2, h3, h4):
    s15 = R_a1d(f"{ph}", f"{th}", f"¬{ch}", h2)
    s20 = R_a1d(f"{ps}", f"{th}", f"¬{ch}", h3)
    s21 = R_pm2_61ii(f"{ph}", f"{ps}", f"→¬{ch}{th}", h1, s15, s20)
    return R_pm2_61i(f"{ch}", f"{th}", h4, s21)

def R_ja(ph, ps, ch, h1, h2):
    s9 = R_imim2i(f"{ps}", f"{ch}", f"{ph}", h2)
    return R_pm2_61d1(f"→{ph}{ps}", f"{ph}", f"{ch}", s9, h1)

def R_jad(ph, ps, ch, th, h1, h2):
    s15 = R_com12(f"{ph}", f"¬{ps}", f"{th}", h1)
    s20 = R_com12(f"{ph}", f"{ch}", f"{th}", h2)
    s21 = R_ja(f"{ps}", f"{ch}", f"→{ph}{th}", s15, s20)
    return R_com12(f"→{ps}{ch}", f"{ph}", f"{th}", s21)

@Theorem(1, "pm2.01")
def R_pm2_01(ph):
    s6 = R_id(f"¬{ph}")
    return R_ja(f"{ph}", f"¬{ph}", f"¬{ph}", s6, s6)

def R_pm2_01i(ph, h1):
    s8 = R_pm2_01(f"{ph}")
    return R_ax_mp(f"→{ph}¬{ph}", f"¬{ph}", h1, s8)

def R_pm2_01d(ph, ps, h1):
    s7 = R_id(f"¬{ps}")
    return R_pm2_61d1(f"{ph}", f"{ps}", f"¬{ps}", h1, s7)

@Theorem(2, "pm2.6")
def R_pm2_6(ph, ps):
    s9 = R_id(f"→¬{ph}{ps}")
    s12 = R_idd(f"→¬{ph}{ps}", f"{ps}")
    return R_jad(f"→¬{ph}{ps}", f"{ph}", f"{ps}", f"{ps}", s9, s12)

@Theorem(2, "pm2.61")
def R_pm2_61(ph, ps):
    s10 = R_pm2_6(f"{ph}", f"{ps}")
    return R_com12(f"→¬{ph}{ps}", f"→{ph}{ps}", f"{ps}", s10)

@Theorem(2, "pm2.65")
def R_pm2_65(ph, ps):
    s12 = R_idd(f"→{ph}{ps}", f"¬{ph}")
    s15 = R_con3(f"{ph}", f"{ps}")
    return R_jad(f"→{ph}{ps}", f"{ph}", f"¬{ps}", f"¬{ph}", s12, s15)

def R_pm2_65i(ph, ps, h1, h2):
    s6 = R_con2i(f"{ph}", f"{ps}", h2)
    s10 = R_con3i(f"{ph}", f"{ps}", h1)
    return R_pm2_61i(f"{ps}", f"¬{ph}", s6, s10)

def R_pm2_21dd(ph, ps, ch, h1, h2):
    s6 = R_pm2_65i(f"{ph}", f"{ps}", h1, h2)
    return R_pm2_21i(f"{ph}", f"{ch}", s6)

def R_pm2_65d(ph, ps, ch, h1, h2):
    s8 = R_nsyld(f"{ph}", f"{ps}", f"{ch}", f"{ps}", h2, h1)
    return R_pm2_01d(f"{ph}", f"{ps}", s8)

def R_mto(ph, ps, h1, h2):
    s7 = R_a1i(f"¬{ps}", f"{ph}", h1)
    return R_pm2_65i(f"{ph}", f"{ps}", h2, s7)

def R_mtod(ph, ps, ch, h1, h2):
    s9 = R_a1d(f"{ph}", f"¬{ch}", f"{ps}", h1)
    return R_pm2_65d(f"{ph}", f"{ps}", f"{ch}", h2, s9)

def R_mtoi(ph, ps, ch, h1, h2):
    s7 = R_a1i(f"¬{ch}", f"{ph}", h1)
    return R_mtod(f"{ph}", f"{ps}", f"{ch}", s7, h2)

def R_mt2(ph, ps, h1, h2):
    s5 = R_a1i(f"{ps}", f"{ph}", h1)
    return R_pm2_65i(f"{ph}", f"{ps}", s5, h2)

def R_mt3(ph, ps, h1, h2):
    s6 = R_mto(f"¬{ph}", f"{ps}", h1, h2)
    return R_notnotri(f"{ph}", s6)

@Theorem(2, "peirce")
def R_peirce(ph, ps):
    s7 = R_simplim(f"{ph}", f"{ps}")
    s9 = R_id(f"{ph}")
    return R_ja(f"→{ph}{ps}", f"{ph}", f"{ph}", s7, s9)

@Theorem(2, "looinv")
def R_looinv(ph, ps):
    s16 = R_imim1(f"→{ph}{ps}", f"{ps}", f"{ph}")
    s19 = R_peirce(f"{ph}", f"{ps}")
    return R_syl6(f"→→{ph}{ps}{ps}", f"→{ps}{ph}", f"→→{ph}{ps}{ph}", f"{ph}", s16, s19)

@Theorem(1, "bijust0")
def R_bijust0(ph):
    s9 = R_id(f"{ph}")
    s11 = R_pm2_01(f"→{ph}{ph}")
    return R_mt2(f"→→{ph}{ph}¬→{ph}{ph}", f"→{ph}{ph}", s9, s11)

@Theorem(2, "bijust")
def R_bijust(ph, ps):
    return R_bijust0(f"¬→→{ph}{ps}¬→{ps}{ph}")

@Theorem(2, "impbi")
def R_impbi(ph, ps):
    s31 = R_df_bi(f"{ph}", f"{ps}")
    s34 = R_simprim(f"→↔{ph}{ps}¬→→{ph}{ps}¬→{ps}{ph}", f"→¬→→{ph}{ps}¬→{ps}{ph}↔{ph}{ps}")
    s35 = R_ax_mp(f"¬→→↔{ph}{ps}¬→→{ph}{ps}¬→{ps}{ph}¬→¬→→{ph}{ps}¬→{ps}{ph}↔{ph}{ps}", f"→¬→→{ph}{ps}¬→{ps}{ph}↔{ph}{ps}", s31, s34)
    return R_expi(f"→{ph}{ps}", f"→{ps}{ph}", f"↔{ph}{ps}", s35)

def R_impbii(ph, ps, h1, h2):
    s13 = R_impbi(f"{ph}", f"{ps}")
    return R_mp2(f"→{ph}{ps}", f"→{ps}{ph}", f"↔{ph}{ps}", h1, h2, s13)

def R_impbidd(ph, ps, ch, th, h1, h2):
    s15 = R_impbi(f"{ch}", f"{th}")
    return R_syl6c(f"{ph}", f"{ps}", f"→{ch}{th}", f"→{th}{ch}", f"↔{ch}{th}", h1, h2, s15)

def R_impbid21d(ph, ps, ch, th, h1, h2):
    s15 = R_impbi(f"{ch}", f"{th}")
    return R_syl2imc(f"{ps}", f"→{ch}{th}", f"{ph}", f"→{th}{ch}", f"↔{ch}{th}", h1, h2, s15)

def R_impbid(ph, ps, ch, h1, h2):
    s10 = R_impbid21d(f"{ph}", f"{ph}", f"{ps}", f"{ch}", h1, h2)
    return R_pm2_43i(f"{ph}", f"↔{ps}{ch}", s10)

@Theorem(2, "dfbi1")
def R_dfbi1(ph, ps):
    s28 = R_df_bi(f"{ph}", f"{ps}")
    s34 = R_impbi(f"↔{ph}{ps}", f"¬→→{ph}{ps}¬→{ps}{ph}")
    s35 = R_con3rr3(f"→↔{ph}{ps}¬→→{ph}{ps}¬→{ps}{ph}", f"→¬→→{ph}{ps}¬→{ps}{ph}↔{ph}{ps}", f"↔↔{ph}{ps}¬→→{ph}{ps}¬→{ps}{ph}", s34)
    return R_mt3(f"↔↔{ph}{ps}¬→→{ph}{ps}¬→{ps}{ph}", f"→→↔{ph}{ps}¬→→{ph}{ps}¬→{ps}{ph}¬→¬→→{ph}{ps}¬→{ps}{ph}↔{ph}{ps}", s28, s35)

@Theorem(2, "biimp")
def R_biimp(ph, ps):
    s31 = R_df_bi(f"{ph}", f"{ps}")
    s34 = R_simplim(f"→↔{ph}{ps}¬→→{ph}{ps}¬→{ps}{ph}", f"¬→¬→→{ph}{ps}¬→{ps}{ph}↔{ph}{ps}")
    s35 = R_ax_mp(f"¬→→↔{ph}{ps}¬→→{ph}{ps}¬→{ps}{ph}¬→¬→→{ph}{ps}¬→{ps}{ph}↔{ph}{ps}", f"→↔{ph}{ps}¬→→{ph}{ps}¬→{ps}{ph}", s31, s34)
    s38 = R_simplim(f"→{ph}{ps}", f"¬→{ps}{ph}")
    return R_syl(f"↔{ph}{ps}", f"¬→→{ph}{ps}¬→{ps}{ph}", f"→{ph}{ps}", s35, s38)

def R_biimpi(ph, ps, h1):
    s9 = R_biimp(f"{ph}", f"{ps}")
    return R_ax_mp(f"↔{ph}{ps}", f"→{ph}{ps}", h1, s9)

def R_sylbi(ph, ps, ch, h1, h2):
    s6 = R_biimpi(f"{ph}", f"{ps}", h1)
    return R_syl(f"{ph}", f"{ps}", f"{ch}", s6, h2)

def R_sylib(ph, ps, ch, h1, h2):
    s7 = R_biimpi(f"{ps}", f"{ch}", h2)
    return R_syl(f"{ph}", f"{ps}", f"{ch}", h1, s7)

def R_sylbb(ph, ps, ch, h1, h2):
    s7 = R_biimpi(f"{ps}", f"{ch}", h2)
    return R_sylbi(f"{ph}", f"{ps}", f"{ch}", h1, s7)

@Theorem(2, "biimpr")
def R_biimpr(ph, ps):
    s17 = R_dfbi1(f"{ph}", f"{ps}")
    s20 = R_simprim(f"→{ph}{ps}", f"→{ps}{ph}")
    return R_sylbi(f"↔{ph}{ps}", f"¬→→{ph}{ps}¬→{ps}{ph}", f"→{ps}{ph}", s17, s20)

@Theorem(2, "bicom1")
def R_bicom1(ph, ps):
    s7 = R_biimpr(f"{ph}", f"{ps}")
    s10 = R_biimp(f"{ph}", f"{ps}")
    return R_impbid(f"↔{ph}{ps}", f"{ps}", f"{ph}", s7, s10)

@Theorem(2, "bicom")
def R_bicom(ph, ps):
    s8 = R_bicom1(f"{ph}", f"{ps}")
    s11 = R_bicom1(f"{ps}", f"{ph}")
    return R_impbii(f"↔{ph}{ps}", f"↔{ps}{ph}", s8, s11)

def R_bicomd(ph, ps, ch, h1):
    s10 = R_bicom(f"{ps}", f"{ch}")
    return R_sylib(f"{ph}", f"↔{ps}{ch}", f"↔{ch}{ps}", h1, s10)

def R_bicomi(ph, ps, h1):
    s9 = R_bicom1(f"{ph}", f"{ps}")
    return R_ax_mp(f"↔{ph}{ps}", f"↔{ps}{ph}", h1, s9)

def R_impbid1(ph, ps, ch, h1, h2):
    s9 = R_a1i(f"→{ch}{ps}", f"{ph}", h2)
    return R_impbid(f"{ph}", f"{ps}", f"{ch}", h1, s9)

def R_impbid2(ph, ps, ch, h1, h2):
    s8 = R_impbid1(f"{ph}", f"{ch}", f"{ps}", h2, h1)
    return R_bicomd(f"{ph}", f"{ch}", f"{ps}", s8)

def R_impcon4bid(ph, ps, ch, h1, h2):
    s8 = R_con4d(f"{ph}", f"{ps}", f"{ch}", h2)
    return R_impbid(f"{ph}", f"{ps}", f"{ch}", h1, s8)

def R_biimpri(ph, ps, h1):
    s5 = R_bicomi(f"{ph}", f"{ps}", h1)
    return R_biimpi(f"{ps}", f"{ph}", s5)

def R_biimpd(ph, ps, ch, h1):
    s10 = R_biimp(f"{ps}", f"{ch}")
    return R_syl(f"{ph}", f"↔{ps}{ch}", f"→{ps}{ch}", h1, s10)

def R_mpbi(ph, ps, h1, h2):
    s6 = R_biimpi(f"{ph}", f"{ps}", h2)
    return R_ax_mp(f"{ph}", f"{ps}", h1, s6)

def R_mpbir(ph, ps, h1, h2):
    s6 = R_biimpri(f"{ph}", f"{ps}", h2)
    return R_ax_mp(f"{ps}", f"{ph}", h1, s6)

def R_mpbid(ph, ps, ch, h1, h2):
    s8 = R_biimpd(f"{ph}", f"{ps}", f"{ch}", h2)
    return R_mpd(f"{ph}", f"{ps}", f"{ch}", h1, s8)

def R_mpbii(ph, ps, ch, h1, h2):
    s6 = R_a1i(f"{ps}", f"{ph}", h1)
    return R_mpbid(f"{ph}", f"{ps}", f"{ch}", s6, h2)

def R_sylibr(ph, ps, ch, h1, h2):
    s7 = R_biimpri(f"{ch}", f"{ps}", h2)
    return R_syl(f"{ph}", f"{ps}", f"{ch}", h1, s7)

def R_sylbir(ph, ps, ch, h1, h2):
    s6 = R_biimpri(f"{ps}", f"{ph}", h1)
    return R_syl(f"{ph}", f"{ps}", f"{ch}", s6, h2)

def R_sylbbr(ph, ps, ch, h1, h2):
    s6 = R_biimpri(f"{ps}", f"{ch}", h2)
    return R_sylibr(f"{ch}", f"{ps}", f"{ph}", s6, h1)

def R_sylbb1(ph, ps, ch, h1, h2):
    s6 = R_biimpri(f"{ph}", f"{ps}", h1)
    return R_sylib(f"{ps}", f"{ph}", f"{ch}", s6, h2)

def R_sylbb2(ph, ps, ch, h1, h2):
    s7 = R_biimpri(f"{ch}", f"{ps}", h2)
    return R_sylbi(f"{ph}", f"{ps}", f"{ch}", h1, s7)

def R_sylibd(ph, ps, ch, th, h1, h2):
    s9 = R_biimpd(f"{ph}", f"{ch}", f"{th}", h2)
    return R_syld(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, s9)

def R_sylbid(ph, ps, ch, th, h1, h2):
    s8 = R_biimpd(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_syld(f"{ph}", f"{ps}", f"{ch}", f"{th}", s8, h2)

def R_mpbidi(ph, ps, ch, th, h1, h2):
    s9 = R_biimpd(f"{ph}", f"{ps}", f"{ch}", h2)
    return R_sylcom(f"{th}", f"{ph}", f"{ps}", f"{ch}", h1, s9)

def R_biimtrid(ph, ps, ch, th, h1, h2):
    s7 = R_biimpi(f"{ph}", f"{ps}", h1)
    return R_syl5(f"{ph}", f"{ps}", f"{ch}", f"{th}", s7, h2)

def R_biimtrrid(ph, ps, ch, th, h1, h2):
    s7 = R_biimpri(f"{ps}", f"{ph}", h1)
    return R_syl5(f"{ph}", f"{ps}", f"{ch}", f"{th}", s7, h2)

def R_imbitrid(ph, ps, ch, th, h1, h2):
    s9 = R_biimpd(f"{ch}", f"{ps}", f"{th}", h2)
    return R_syl5(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, s9)

def R_syl5ibcom(ph, ps, ch, th, h1, h2):
    s9 = R_imbitrid(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2)
    return R_com12(f"{ch}", f"{ph}", f"{th}", s9)

def R_imbitrrid(ph, ps, ch, th, h1, h2):
    s9 = R_bicomd(f"{ch}", f"{ps}", f"{th}", h2)
    return R_imbitrid(f"{ph}", f"{th}", f"{ch}", f"{ps}", h1, s9)

def R_syl5ibrcom(ph, ps, ch, th, h1, h2):
    s9 = R_imbitrrid(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2)
    return R_com12(f"{ch}", f"{ph}", f"{ps}", s9)

def R_biimprd(ph, ps, ch, h1):
    s5 = R_id(f"{ch}")
    return R_imbitrrid(f"{ch}", f"{ps}", f"{ph}", f"{ch}", s5, h1)

def R_biimpcd(ph, ps, ch, h1):
    s5 = R_id(f"{ps}")
    return R_syl5ibcom(f"{ps}", f"{ps}", f"{ph}", f"{ch}", s5, h1)

def R_biimprcd(ph, ps, ch, h1):
    s5 = R_id(f"{ch}")
    return R_syl5ibrcom(f"{ch}", f"{ps}", f"{ph}", f"{ch}", s5, h1)

def R_imbitrdi(ph, ps, ch, th, h1, h2):
    s8 = R_biimpi(f"{ch}", f"{th}", h2)
    return R_syl6(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, s8)

def R_imbitrrdi(ph, ps, ch, th, h1, h2):
    s8 = R_biimpri(f"{th}", f"{ch}", h2)
    return R_syl6(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, s8)

def R_biimtrdi(ph, ps, ch, th, h1, h2):
    s8 = R_biimpd(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_syl6(f"{ph}", f"{ps}", f"{ch}", f"{th}", s8, h2)

def R_biimtrrdi(ph, ps, ch, th, h1, h2):
    s8 = R_biimprd(f"{ph}", f"{ch}", f"{ps}", h1)
    return R_syl6(f"{ph}", f"{ps}", f"{ch}", f"{th}", s8, h2)

def R_syl7bi(ph, ps, ch, th, ta, h1, h2):
    s8 = R_biimpi(f"{ph}", f"{ps}", h1)
    return R_syl7(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", s8, h2)

def R_syl8ib(ph, ps, ch, th, ta, h1, h2):
    s9 = R_biimpi(f"{th}", f"{ta}", h2)
    return R_syl8(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1, s9)

def R_mpbird(ph, ps, ch, h1, h2):
    s8 = R_biimprd(f"{ph}", f"{ps}", f"{ch}", h2)
    return R_mpd(f"{ph}", f"{ch}", f"{ps}", h1, s8)

def R_mpbiri(ph, ps, ch, h1, h2):
    s6 = R_a1i(f"{ch}", f"{ph}", h1)
    return R_mpbird(f"{ph}", f"{ps}", f"{ch}", s6, h2)

def R_sylibrd(ph, ps, ch, th, h1, h2):
    s9 = R_biimprd(f"{ph}", f"{th}", f"{ch}", h2)
    return R_syld(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, s9)

def R_sylbird(ph, ps, ch, th, h1, h2):
    s8 = R_biimprd(f"{ph}", f"{ch}", f"{ps}", h1)
    return R_syld(f"{ph}", f"{ps}", f"{ch}", f"{th}", s8, h2)

@Theorem(1, "biid")
def R_biid(ph):
    s3 = R_id(f"{ph}")
    return R_impbii(f"{ph}", f"{ph}", s3, s3)

@Theorem(2, "biidd")
def R_biidd(ph, ps):
    s5 = R_biid(f"{ps}")
    return R_a1i(f"↔{ps}{ps}", f"{ph}", s5)

@Theorem(2, "pm5.1im")
def R_pm5_1im(ph, ps):
    s6 = R_ax_1(f"{ps}", f"{ph}")
    s9 = R_ax_1(f"{ph}", f"{ps}")
    return R_impbid21d(f"{ph}", f"{ps}", f"{ph}", f"{ps}", s6, s9)

def R_2th(ph, ps, h1, h2):
    s5 = R_a1i(f"{ps}", f"{ph}", h2)
    s9 = R_a1i(f"{ph}", f"{ps}", h1)
    return R_impbii(f"{ph}", f"{ps}", s5, s9)

def R_2thd(ph, ps, ch, h1, h2):
    s10 = R_pm5_1im(f"{ps}", f"{ch}")
    return R_sylc(f"{ph}", f"{ps}", f"{ch}", f"↔{ps}{ch}", h1, h2, s10)

@Theorem(2, "monothetic")
def R_monothetic(ph, ps):
    s7 = R_id(f"{ph}")
    s9 = R_id(f"{ps}")
    return R_2th(f"→{ph}{ph}", f"→{ps}{ps}", s7, s9)

def R_ibi(ph, ps, h1):
    s4 = R_id(f"{ph}")
    return R_mpbid(f"{ph}", f"{ph}", f"{ps}", s4, h1)

def R_ibir(ph, ps, h1):
    s6 = R_bicomd(f"{ph}", f"{ps}", f"{ph}", h1)
    return R_ibi(f"{ph}", f"{ps}", s6)

def R_ibd(ph, ps, ch, h1):
    s9 = R_biimp(f"{ps}", f"{ch}")
    return R_syli(f"{ps}", f"{ph}", f"↔{ps}{ch}", f"{ch}", h1, s9)

@Theorem(3, "pm5.74")
def R_pm5_74(ph, ps, ch):
    s26 = R_biimp(f"{ps}", f"{ch}")
    s27 = R_imim3i(f"↔{ps}{ch}", f"{ps}", f"{ch}", f"{ph}", s26)
    s34 = R_biimpr(f"{ps}", f"{ch}")
    s35 = R_imim3i(f"↔{ps}{ch}", f"{ch}", f"{ps}", f"{ph}", s34)
    s36 = R_impbid(f"→{ph}↔{ps}{ch}", f"→{ph}{ps}", f"→{ph}{ch}", s27, s35)
    s47 = R_biimp(f"→{ph}{ps}", f"→{ph}{ch}")
    s48 = R_pm2_86d(f"↔→{ph}{ps}→{ph}{ch}", f"{ph}", f"{ps}", f"{ch}", s47)
    s55 = R_biimpr(f"→{ph}{ps}", f"→{ph}{ch}")
    s56 = R_pm2_86d(f"↔→{ph}{ps}→{ph}{ch}", f"{ph}", f"{ch}", f"{ps}", s55)
    s57 = R_impbidd(f"↔→{ph}{ps}→{ph}{ch}", f"{ph}", f"{ps}", f"{ch}", s48, s56)
    return R_impbii(f"→{ph}↔{ps}{ch}", f"↔→{ph}{ps}→{ph}{ch}", s36, s57)

def R_pm5_74i(ph, ps, ch, h1):
    s16 = R_pm5_74(f"{ph}", f"{ps}", f"{ch}")
    return R_mpbi(f"→{ph}↔{ps}{ch}", f"↔→{ph}{ps}→{ph}{ch}", h1, s16)

def R_pm5_74ri(ph, ps, ch, h1):
    s16 = R_pm5_74(f"{ph}", f"{ps}", f"{ch}")
    return R_mpbir(f"→{ph}↔{ps}{ch}", f"↔→{ph}{ps}→{ph}{ch}", h1, s16)

def R_pm5_74d(ph, ps, ch, th, h1):
    s17 = R_pm5_74(f"{ps}", f"{ch}", f"{th}")
    return R_sylib(f"{ph}", f"→{ps}↔{ch}{th}", f"↔→{ps}{ch}→{ps}{th}", h1, s17)

def R_pm5_74rd(ph, ps, ch, th, h1):
    s17 = R_pm5_74(f"{ps}", f"{ch}", f"{th}")
    return R_sylibr(f"{ph}", f"↔→{ps}{ch}→{ps}{th}", f"→{ps}↔{ch}{th}", h1, s17)

def R_bitri(ph, ps, ch, h1, h2):
    s7 = R_sylbb(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    s13 = R_sylbbr(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    return R_impbii(f"{ph}", f"{ch}", s7, s13)

def R_bitr2i(ph, ps, ch, h1, h2):
    s7 = R_bitri(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    return R_bicomi(f"{ph}", f"{ch}", s7)

def R_bitr3i(ph, ps, ch, h1, h2):
    s6 = R_bicomi(f"{ps}", f"{ph}", h1)
    return R_bitri(f"{ph}", f"{ps}", f"{ch}", s6, h2)

def R_bitr4i(ph, ps, ch, h1, h2):
    s7 = R_bicomi(f"{ch}", f"{ps}", h2)
    return R_bitri(f"{ph}", f"{ps}", f"{ch}", h1, s7)

def R_bitrd(ph, ps, ch, th, h1, h2):
    s16 = R_pm5_74i(f"{ph}", f"{ps}", f"{ch}", h1)
    s21 = R_pm5_74i(f"{ph}", f"{ch}", f"{th}", h2)
    s22 = R_bitri(f"→{ph}{ps}", f"→{ph}{ch}", f"→{ph}{th}", s16, s21)
    return R_pm5_74ri(f"{ph}", f"{ps}", f"{th}", s22)

def R_bitr2d(ph, ps, ch, th, h1, h2):
    s9 = R_bitrd(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2)
    return R_bicomd(f"{ph}", f"{ps}", f"{th}", s9)

def R_bitr3d(ph, ps, ch, th, h1, h2):
    s8 = R_bicomd(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_bitrd(f"{ph}", f"{ch}", f"{ps}", f"{th}", s8, h2)

def R_bitr4d(ph, ps, ch, th, h1, h2):
    s9 = R_bicomd(f"{ph}", f"{th}", f"{ch}", h2)
    return R_bitrd(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, s9)

def R_bitrid(ph, ps, ch, th, h1, h2):
    s9 = R_a1i(f"↔{ph}{ps}", f"{ch}", h1)
    return R_bitrd(f"{ch}", f"{ph}", f"{ps}", f"{th}", s9, h2)

def R_bitr2id(ph, ps, ch, th, h1, h2):
    s9 = R_bitrid(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2)
    return R_bicomd(f"{ch}", f"{ph}", f"{th}", s9)

def R_bitr3id(ph, ps, ch, th, h1, h2):
    s7 = R_bicomi(f"{ps}", f"{ph}", h1)
    return R_bitrid(f"{ph}", f"{ps}", f"{ch}", f"{th}", s7, h2)

def R_bitr3di(ph, ps, ch, th, h1, h2):
    s7 = R_bicomi(f"{ps}", f"{th}", h2)
    return R_bitr2id(f"{th}", f"{ps}", f"{ph}", f"{ch}", s7, h1)

def R_bitrdi(ph, ps, ch, th, h1, h2):
    s10 = R_a1i(f"↔{ch}{th}", f"{ph}", h2)
    return R_bitrd(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, s10)

def R_bitr2di(ph, ps, ch, th, h1, h2):
    s9 = R_bitrdi(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2)
    return R_bicomd(f"{ph}", f"{ps}", f"{th}", s9)

def R_bitr4di(ph, ps, ch, th, h1, h2):
    s8 = R_bicomi(f"{th}", f"{ch}", h2)
    return R_bitrdi(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, s8)

def R_bitr4id(ph, ps, ch, th, h1, h2):
    s8 = R_bicomi(f"{ps}", f"{ch}", h1)
    return R_bitr2di(f"{ph}", f"{th}", f"{ch}", f"{ps}", h2, s8)

def R_3imtr3i(ph, ps, ch, th, h1, h2, h3):
    s8 = R_sylbir(f"{ch}", f"{ph}", f"{ps}", h2, h1)
    return R_sylib(f"{ch}", f"{ps}", f"{th}", s8, h3)

def R_3imtr4i(ph, ps, ch, th, h1, h2, h3):
    s8 = R_sylbi(f"{ch}", f"{ph}", f"{ps}", h2, h1)
    return R_sylibr(f"{ch}", f"{ps}", f"{th}", s8, h3)

def R_3imtr3d(ph, ps, ch, th, ta, h1, h2, h3):
    s11 = R_sylibd(f"{ph}", f"{ps}", f"{ch}", f"{ta}", h1, h3)
    return R_sylbird(f"{ph}", f"{th}", f"{ps}", f"{ta}", h2, s11)

def R_3imtr4d(ph, ps, ch, th, ta, h1, h2, h3):
    s11 = R_sylibrd(f"{ph}", f"{ps}", f"{ch}", f"{ta}", h1, h3)
    return R_sylbid(f"{ph}", f"{th}", f"{ps}", f"{ta}", h2, s11)

def R_3imtr3g(ph, ps, ch, th, ta, h1, h2, h3):
    s10 = R_biimtrrid(f"{th}", f"{ps}", f"{ph}", f"{ch}", h2, h1)
    return R_imbitrdi(f"{ph}", f"{th}", f"{ch}", f"{ta}", s10, h3)

def R_3imtr4g(ph, ps, ch, th, ta, h1, h2, h3):
    s10 = R_biimtrid(f"{th}", f"{ps}", f"{ph}", f"{ch}", h2, h1)
    return R_imbitrrdi(f"{ph}", f"{th}", f"{ch}", f"{ta}", s10, h3)

def R_3bitri(ph, ps, ch, th, h1, h2, h3):
    s9 = R_bitri(f"{ps}", f"{ch}", f"{th}", h2, h3)
    return R_bitri(f"{ph}", f"{ps}", f"{th}", h1, s9)

def R_3bitrri(ph, ps, ch, th, h1, h2, h3):
    s9 = R_bitr2i(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    return R_bitr3i(f"{th}", f"{ch}", f"{ph}", h3, s9)

def R_3bitr2i(ph, ps, ch, th, h1, h2, h3):
    s8 = R_bitr4i(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    return R_bitri(f"{ph}", f"{ch}", f"{th}", s8, h3)

def R_3bitr2ri(ph, ps, ch, th, h1, h2, h3):
    s8 = R_bitr4i(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    return R_bitr2i(f"{ph}", f"{ch}", f"{th}", s8, h3)

def R_3bitr3i(ph, ps, ch, th, h1, h2, h3):
    s8 = R_bitr3i(f"{ch}", f"{ph}", f"{ps}", h2, h1)
    return R_bitri(f"{ch}", f"{ps}", f"{th}", s8, h3)

def R_3bitr3ri(ph, ps, ch, th, h1, h2, h3):
    s9 = R_bitr3i(f"{ps}", f"{ph}", f"{ch}", h1, h2)
    return R_bitr3i(f"{th}", f"{ps}", f"{ch}", h3, s9)

def R_3bitr4i(ph, ps, ch, th, h1, h2, h3):
    s9 = R_bitr4i(f"{ph}", f"{ps}", f"{th}", h1, h3)
    return R_bitri(f"{ch}", f"{ph}", f"{th}", h2, s9)

def R_3bitr4ri(ph, ps, ch, th, h1, h2, h3):
    s9 = R_bitr4i(f"{ph}", f"{ps}", f"{th}", h1, h3)
    return R_bitr2i(f"{ch}", f"{ph}", f"{th}", h2, s9)

def R_3bitrd(ph, ps, ch, th, ta, h1, h2, h3):
    s10 = R_bitrd(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2)
    return R_bitrd(f"{ph}", f"{ps}", f"{th}", f"{ta}", s10, h3)

def R_3bitrrd(ph, ps, ch, th, ta, h1, h2, h3):
    s11 = R_bitr2d(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2)
    return R_bitr3d(f"{ph}", f"{th}", f"{ta}", f"{ps}", h3, s11)

def R_3bitr2d(ph, ps, ch, th, ta, h1, h2, h3):
    s10 = R_bitr4d(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2)
    return R_bitrd(f"{ph}", f"{ps}", f"{th}", f"{ta}", s10, h3)

def R_3bitr2rd(ph, ps, ch, th, ta, h1, h2, h3):
    s10 = R_bitr4d(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2)
    return R_bitr2d(f"{ph}", f"{ps}", f"{th}", f"{ta}", s10, h3)

def R_3bitr3d(ph, ps, ch, th, ta, h1, h2, h3):
    s10 = R_bitr3d(f"{ph}", f"{ps}", f"{th}", f"{ch}", h2, h1)
    return R_bitrd(f"{ph}", f"{th}", f"{ch}", f"{ta}", s10, h3)

def R_3bitr3rd(ph, ps, ch, th, ta, h1, h2, h3):
    s11 = R_bitr3d(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2)
    return R_bitr3d(f"{ph}", f"{ch}", f"{ta}", f"{th}", h3, s11)

def R_3bitr4d(ph, ps, ch, th, ta, h1, h2, h3):
    s11 = R_bitr4d(f"{ph}", f"{ps}", f"{ch}", f"{ta}", h1, h3)
    return R_bitrd(f"{ph}", f"{th}", f"{ps}", f"{ta}", h2, s11)

def R_3bitr4rd(ph, ps, ch, th, ta, h1, h2, h3):
    s10 = R_bitr4d(f"{ph}", f"{ta}", f"{ch}", f"{ps}", h3, h1)
    return R_bitr4d(f"{ph}", f"{ta}", f"{ps}", f"{th}", s10, h2)

def R_3bitr3g(ph, ps, ch, th, ta, h1, h2, h3):
    s10 = R_bitr3id(f"{th}", f"{ps}", f"{ph}", f"{ch}", h2, h1)
    return R_bitrdi(f"{ph}", f"{th}", f"{ch}", f"{ta}", s10, h3)

def R_3bitr4g(ph, ps, ch, th, ta, h1, h2, h3):
    s10 = R_bitrid(f"{th}", f"{ps}", f"{ph}", f"{ch}", h2, h1)
    return R_bitr4di(f"{ph}", f"{th}", f"{ch}", f"{ta}", s10, h3)

@Theorem(1, "notnotb")
def R_notnotb(ph):
    s5 = R_notnot(f"{ph}")
    s7 = R_notnotr(f"{ph}")
    return R_impbii(f"{ph}", f"¬¬{ph}", s5, s7)

@Theorem(2, "con34b")
def R_con34b(ph, ps):
    s10 = R_con3(f"{ph}", f"{ps}")
    s13 = R_con4(f"{ps}", f"{ph}")
    return R_impbii(f"→{ph}{ps}", f"→¬{ps}¬{ph}", s10, s13)

def R_con4bid(ph, ps, ch, h1):
    s14 = R_biimprd(f"{ph}", f"¬{ps}", f"¬{ch}", h1)
    s15 = R_con4d(f"{ph}", f"{ch}", f"{ps}", s14)
    s20 = R_biimpd(f"{ph}", f"¬{ps}", f"¬{ch}", h1)
    return R_impcon4bid(f"{ph}", f"{ps}", f"{ch}", s15, s20)

def R_notbid(ph, ps, ch, h1):
    s16 = R_notnotb(f"{ps}")
    s18 = R_notnotb(f"{ch}")
    s19 = R_3bitr3g(f"{ph}", f"{ps}", f"{ch}", f"¬¬{ps}", f"¬¬{ch}", h1, s16, s18)
    return R_con4bid(f"{ph}", f"¬{ps}", f"¬{ch}", s19)

@Theorem(2, "notbi")
def R_notbi(ph, ps):
    s14 = R_id(f"↔{ph}{ps}")
    s15 = R_notbid(f"↔{ph}{ps}", f"{ph}", f"{ps}", s14)
    s20 = R_id(f"↔¬{ph}¬{ps}")
    s21 = R_con4bid(f"↔¬{ph}¬{ps}", f"{ph}", f"{ps}", s20)
    return R_impbii(f"↔{ph}{ps}", f"↔¬{ph}¬{ps}", s15, s21)

def R_notbii(ph, ps, h1):
    s11 = R_notbi(f"{ph}", f"{ps}")
    return R_mpbi(f"↔{ph}{ps}", f"↔¬{ph}¬{ps}", h1, s11)

def R_con4bii(ph, ps, h1):
    s11 = R_notbi(f"{ph}", f"{ps}")
    return R_mpbir(f"↔{ph}{ps}", f"↔¬{ph}¬{ps}", h1, s11)

def R_mtbi(ph, ps, h1, h2):
    s6 = R_biimpri(f"{ph}", f"{ps}", h2)
    return R_mto(f"{ps}", f"{ph}", h1, s6)

def R_mtbir(ph, ps, h1, h2):
    s6 = R_bicomi(f"{ph}", f"{ps}", h2)
    return R_mtbi(f"{ps}", f"{ph}", h1, s6)

def R_mtbid(ph, ps, ch, h1, h2):
    s8 = R_biimprd(f"{ph}", f"{ps}", f"{ch}", h2)
    return R_mtod(f"{ph}", f"{ch}", f"{ps}", h1, s8)

def R_mtbird(ph, ps, ch, h1, h2):
    s8 = R_biimpd(f"{ph}", f"{ps}", f"{ch}", h2)
    return R_mtod(f"{ph}", f"{ps}", f"{ch}", h1, s8)

def R_mtbii(ph, ps, ch, h1, h2):
    s8 = R_biimprd(f"{ph}", f"{ps}", f"{ch}", h2)
    return R_mtoi(f"{ph}", f"{ch}", f"{ps}", h1, s8)

def R_mtbiri(ph, ps, ch, h1, h2):
    s8 = R_biimpd(f"{ph}", f"{ps}", f"{ch}", h2)
    return R_mtoi(f"{ph}", f"{ps}", f"{ch}", h1, s8)

def R_sylnib(ph, ps, ch, h1, h2):
    s7 = R_biimpri(f"{ps}", f"{ch}", h2)
    return R_nsyl(f"{ph}", f"{ps}", f"{ch}", h1, s7)

def R_sylnibr(ph, ps, ch, h1, h2):
    s7 = R_bicomi(f"{ch}", f"{ps}", h2)
    return R_sylnib(f"{ph}", f"{ps}", f"{ch}", h1, s7)

def R_sylnbi(ph, ps, ch, h1, h2):
    s8 = R_notbii(f"{ph}", f"{ps}", h1)
    return R_sylbi(f"¬{ph}", f"¬{ps}", f"{ch}", s8, h2)

def R_sylnbir(ph, ps, ch, h1, h2):
    s6 = R_bicomi(f"{ps}", f"{ph}", h1)
    return R_sylnbi(f"{ph}", f"{ps}", f"{ch}", s6, h2)

def R_xchnxbi(ph, ps, ch, h1, h2):
    s8 = R_notbii(f"{ph}", f"{ch}", h2)
    return R_bitr3i(f"¬{ch}", f"¬{ph}", f"{ps}", s8, h1)

def R_xchnxbir(ph, ps, ch, h1, h2):
    s7 = R_bicomi(f"{ch}", f"{ph}", h2)
    return R_xchnxbi(f"{ph}", f"{ps}", f"{ch}", h1, s7)

def R_xchbinx(ph, ps, ch, h1, h2):
    s9 = R_notbii(f"{ps}", f"{ch}", h2)
    return R_bitri(f"{ph}", f"¬{ps}", f"¬{ch}", h1, s9)

def R_xchbinxr(ph, ps, ch, h1, h2):
    s7 = R_bicomi(f"{ch}", f"{ps}", h2)
    return R_xchbinx(f"{ph}", f"{ps}", f"{ch}", h1, s7)

def R_imbi2i(ph, ps, ch, h1):
    s8 = R_a1i(f"↔{ph}{ps}", f"{ch}", h1)
    return R_pm5_74i(f"{ch}", f"{ph}", f"{ps}", s8)

def R_bibi2i(ph, ps, ch, h1):
    s13 = R_id(f"↔{ch}{ph}")
    s15 = R_bitrdi(f"↔{ch}{ph}", f"{ch}", f"{ph}", f"{ps}", s13, h1)
    s21 = R_id(f"↔{ch}{ps}")
    s23 = R_bitr4di(f"↔{ch}{ps}", f"{ch}", f"{ps}", f"{ph}", s21, h1)
    return R_impbii(f"↔{ch}{ph}", f"↔{ch}{ps}", s15, s23)

def R_bibi1i(ph, ps, ch, h1):
    s14 = R_bicom(f"{ph}", f"{ch}")
    s19 = R_bibi2i(f"{ph}", f"{ps}", f"{ch}", h1)
    s22 = R_bicom(f"{ch}", f"{ps}")
    return R_3bitri(f"↔{ph}{ch}", f"↔{ch}{ph}", f"↔{ch}{ps}", f"↔{ps}{ch}", s14, s19, s22)

def R_bibi12i(ph, ps, ch, th, h1, h2):
    s13 = R_bibi2i(f"{ch}", f"{th}", f"{ph}", h2)
    s18 = R_bibi1i(f"{ph}", f"{ps}", f"{th}", h1)
    return R_bitri(f"↔{ph}{ch}", f"↔{ph}{th}", f"↔{ps}{th}", s13, s18)

def R_imbi2d(ph, ps, ch, th, h1):
    s10 = R_a1d(f"{ph}", f"↔{ps}{ch}", f"{th}", h1)
    return R_pm5_74d(f"{ph}", f"{th}", f"{ps}", f"{ch}", s10)

def R_imbi1d(ph, ps, ch, th, h1):
    s15 = R_biimprd(f"{ph}", f"{ps}", f"{ch}", h1)
    s16 = R_imim1d(f"{ph}", f"{ch}", f"{ps}", f"{th}", s15)
    s25 = R_biimpd(f"{ph}", f"{ps}", f"{ch}", h1)
    s26 = R_imim1d(f"{ph}", f"{ps}", f"{ch}", f"{th}", s25)
    return R_impbid(f"{ph}", f"→{ps}{th}", f"→{ch}{th}", s16, s26)

def R_bibi2d(ph, ps, ch, th, h1):
    s37 = R_pm5_74i(f"{ph}", f"{ps}", f"{ch}", h1)
    s38 = R_bibi2i(f"→{ph}{ps}", f"→{ph}{ch}", f"→{ph}{th}", s37)
    s42 = R_pm5_74(f"{ph}", f"{th}", f"{ps}")
    s46 = R_pm5_74(f"{ph}", f"{th}", f"{ch}")
    s47 = R_3bitr4i(f"↔→{ph}{th}→{ph}{ps}", f"↔→{ph}{th}→{ph}{ch}", f"→{ph}↔{th}{ps}", f"→{ph}↔{th}{ch}", s38, s42, s46)
    return R_pm5_74ri(f"{ph}", f"↔{th}{ps}", f"↔{th}{ch}", s47)

def R_bibi1d(ph, ps, ch, th, h1):
    s18 = R_bibi2d(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    s21 = R_bicom(f"{ps}", f"{th}")
    s24 = R_bicom(f"{ch}", f"{th}")
    return R_3bitr4g(f"{ph}", f"↔{th}{ps}", f"↔{th}{ch}", f"↔{ps}{th}", f"↔{ch}{th}", s18, s21, s24)

def R_imbi12d(ph, ps, ch, th, ta, h1, h2):
    s15 = R_imbi1d(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    s21 = R_imbi2d(f"{ph}", f"{th}", f"{ta}", f"{ch}", h2)
    return R_bitrd(f"{ph}", f"→{ps}{th}", f"→{ch}{th}", f"→{ch}{ta}", s15, s21)

def R_bibi12d(ph, ps, ch, th, ta, h1, h2):
    s15 = R_bibi1d(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    s21 = R_bibi2d(f"{ph}", f"{th}", f"{ta}", f"{ch}", h2)
    return R_bitrd(f"{ph}", f"↔{ps}{th}", f"↔{ch}{th}", f"↔{ch}{ta}", s15, s21)

@Theorem(4, "imbi12")
def R_imbi12(ph, ps, ch, th):
    s27 = R_simplim(f"↔{ph}{ps}", f"¬↔{ch}{th}")
    s30 = R_simprim(f"↔{ph}{ps}", f"↔{ch}{th}")
    s31 = R_imbi12d(f"¬→↔{ph}{ps}¬↔{ch}{th}", f"{ph}", f"{ps}", f"{ch}", f"{th}", s27, s30)
    return R_expi(f"↔{ph}{ps}", f"↔{ch}{th}", f"↔→{ph}{ch}→{ps}{th}", s31)

@Theorem(3, "imbi1")
def R_imbi1(ph, ps, ch):
    s8 = R_id(f"↔{ph}{ps}")
    return R_imbi1d(f"↔{ph}{ps}", f"{ph}", f"{ps}", f"{ch}", s8)

@Theorem(3, "imbi2")
def R_imbi2(ph, ps, ch):
    s8 = R_id(f"↔{ph}{ps}")
    return R_imbi2d(f"↔{ph}{ps}", f"{ph}", f"{ps}", f"{ch}", s8)

def R_imbi1i(ph, ps, ch, h1):
    s14 = R_imbi1(f"{ph}", f"{ps}", f"{ch}")
    return R_ax_mp(f"↔{ph}{ps}", f"↔→{ph}{ch}→{ps}{ch}", h1, s14)

def R_imbi12i(ph, ps, ch, th, h1, h2):
    s19 = R_imbi12(f"{ph}", f"{ps}", f"{ch}", f"{th}")
    return R_mp2(f"↔{ph}{ps}", f"↔{ch}{th}", f"↔→{ph}{ch}→{ps}{th}", h1, h2, s19)

@Theorem(3, "bibi1")
def R_bibi1(ph, ps, ch):
    s8 = R_id(f"↔{ph}{ps}")
    return R_bibi1d(f"↔{ph}{ps}", f"{ph}", f"{ps}", f"{ch}", s8)

@Theorem(3, "bitr3")
def R_bitr3(ph, ps, ch):
    s12 = R_bibi1(f"{ph}", f"{ps}", f"{ch}")
    return R_biimpd(f"↔{ph}{ps}", f"↔{ph}{ch}", f"↔{ps}{ch}", s12)

@Theorem(2, "con2bi")
def R_con2bi(ph, ps):
    s20 = R_notbi(f"{ph}", f"¬{ps}")
    s25 = R_notnotb(f"{ps}")
    s26 = R_bibi2i(f"{ps}", f"¬¬{ps}", f"¬{ph}", s25)
    s29 = R_bicom(f"¬{ph}", f"{ps}")
    return R_3bitr2i(f"↔{ph}¬{ps}", f"↔¬{ph}¬¬{ps}", f"↔¬{ph}{ps}", f"↔{ps}¬{ph}", s20, s26, s29)

def R_con2bid(ph, ps, ch, h1):
    s12 = R_con2bi(f"{ch}", f"{ps}")
    return R_sylibr(f"{ph}", f"↔{ps}¬{ch}", f"↔{ch}¬{ps}", h1, s12)

def R_con1bid(ph, ps, ch, h1):
    s12 = R_bicomd(f"{ph}", f"¬{ps}", f"{ch}", h1)
    s13 = R_con2bid(f"{ph}", f"{ch}", f"{ps}", s12)
    return R_bicomd(f"{ph}", f"{ps}", f"¬{ch}", s13)

def R_con1bii(ph, ps, h1):
    s8 = R_notnotb(f"{ph}")
    s10 = R_xchbinx(f"{ph}", f"¬{ph}", f"{ps}", s8, h1)
    return R_bicomi(f"{ph}", f"¬{ps}", s10)

def R_con2bii(ph, ps, h1):
    s5 = R_notnotb(f"{ps}")
    return R_xchbinxr(f"{ps}", f"¬{ps}", f"{ph}", s5, h1)

@Theorem(2, "con1b")
def R_con1b(ph, ps):
    s10 = R_con1(f"{ph}", f"{ps}")
    s13 = R_con1(f"{ps}", f"{ph}")
    return R_impbii(f"→¬{ph}{ps}", f"→¬{ps}{ph}", s10, s13)

@Theorem(2, "con2b")
def R_con2b(ph, ps):
    s10 = R_con2(f"{ph}", f"{ps}")
    s13 = R_con2(f"{ps}", f"{ph}")
    return R_impbii(f"→{ph}¬{ps}", f"→{ps}¬{ph}", s10, s13)

@Theorem(2, "biimt")
def R_biimt(ph, ps):
    s7 = R_ax_1(f"{ps}", f"{ph}")
    s10 = R_pm2_27(f"{ph}", f"{ps}")
    return R_impbid2(f"{ph}", f"{ps}", f"→{ph}{ps}", s7, s10)

@Theorem(2, "pm5.5")
def R_pm5_5(ph, ps):
    s7 = R_biimt(f"{ph}", f"{ps}")
    return R_bicomd(f"{ph}", f"{ps}", f"→{ph}{ps}", s7)

def R_a1bi(ph, ps, h1):
    s9 = R_biimt(f"{ph}", f"{ps}")
    return R_ax_mp(f"{ph}", f"↔{ps}→{ph}{ps}", h1, s9)

def R_mt2bi(ph, ps, h1):
    s13 = R_a1bi(f"{ph}", f"¬{ps}", h1)
    s16 = R_con2b(f"{ph}", f"{ps}")
    return R_bitri(f"¬{ps}", f"→{ph}¬{ps}", f"→{ps}¬{ph}", s13, s16)

@Theorem(2, "mtt")
def R_mtt(ph, ps):
    s14 = R_biimt(f"¬{ph}", f"¬{ps}")
    s17 = R_con34b(f"{ps}", f"{ph}")
    return R_bitr4di(f"¬{ph}", f"¬{ps}", f"→¬{ph}¬{ps}", f"→{ps}{ph}", s14, s17)

@Theorem(2, "imnot")
def R_imnot(ph, ps):
    s9 = R_mtt(f"{ps}", f"{ph}")
    return R_bicomd(f"¬{ps}", f"¬{ph}", f"→{ph}{ps}", s9)

@Theorem(2, "pm5.501")
def R_pm5_501(ph, ps):
    s8 = R_pm5_1im(f"{ph}", f"{ps}")
    s14 = R_biimp(f"{ph}", f"{ps}")
    s15 = R_com12(f"↔{ph}{ps}", f"{ph}", f"{ps}", s14)
    return R_impbid(f"{ph}", f"{ps}", f"↔{ph}{ps}", s8, s15)

@Theorem(2, "ibib")
def R_ibib(ph, ps):
    s7 = R_pm5_501(f"{ph}", f"{ps}")
    return R_pm5_74i(f"{ph}", f"{ps}", f"↔{ph}{ps}", s7)

@Theorem(2, "ibibr")
def R_ibibr(ph, ps):
    s14 = R_pm5_501(f"{ph}", f"{ps}")
    s17 = R_bicom(f"{ph}", f"{ps}")
    s18 = R_bitrdi(f"{ph}", f"{ps}", f"↔{ph}{ps}", f"↔{ps}{ph}", s14, s17)
    return R_pm5_74i(f"{ph}", f"{ps}", f"↔{ps}{ph}", s18)

def R_tbt(ph, ps, h1):
    s13 = R_ibibr(f"{ph}", f"{ps}")
    s14 = R_pm5_74ri(f"{ph}", f"{ps}", f"↔{ps}{ph}", s13)
    return R_ax_mp(f"{ph}", f"↔{ps}↔{ps}{ph}", h1, s14)

@Theorem(2, "nbn2")
def R_nbn2(ph, ps):
    s14 = R_pm5_501(f"¬{ph}", f"¬{ps}")
    s17 = R_notbi(f"{ph}", f"{ps}")
    return R_bitr4di(f"¬{ph}", f"¬{ps}", f"↔¬{ph}¬{ps}", f"↔{ph}{ps}", s14, s17)

@Theorem(2, "bibif")
def R_bibif(ph, ps):
    s12 = R_nbn2(f"{ps}", f"{ph}")
    s15 = R_bicom(f"{ps}", f"{ph}")
    return R_bitr2di(f"¬{ps}", f"¬{ph}", f"↔{ps}{ph}", f"↔{ph}{ps}", s12, s15)

def R_nbn(ph, ps, h1):
    s15 = R_bibif(f"{ps}", f"{ph}")
    s16 = R_ax_mp(f"¬{ph}", f"↔↔{ps}{ph}¬{ps}", h1, s15)
    return R_bicomi(f"↔{ps}{ph}", f"¬{ps}", s16)

def R_nbn3(ph, ps, h1):
    s5 = R_notnoti(f"{ph}", h1)
    return R_nbn(f"¬{ph}", f"{ps}", s5)

@Theorem(2, "pm5.21im")
def R_pm5_21im(ph, ps):
    s9 = R_nbn2(f"{ph}", f"{ps}")
    return R_biimpd(f"¬{ph}", f"¬{ps}", f"↔{ph}{ps}", s9)

def R_2false(ph, ps, h1, h2):
    s8 = R_2th(f"¬{ph}", f"¬{ps}", h1, h2)
    return R_con4bii(f"{ph}", f"{ps}", s8)

def R_2falsed(ph, ps, ch, h1, h2):
    s10 = R_2thd(f"{ph}", f"¬{ps}", f"¬{ch}", h1, h2)
    return R_con4bid(f"{ph}", f"{ps}", f"{ch}", s10)

def R_pm5_21ni(ph, ps, ch, h1, h2):
    s7 = R_con3i(f"{ph}", f"{ps}", h1)
    s11 = R_con3i(f"{ch}", f"{ps}", h2)
    return R_2falsed(f"¬{ps}", f"{ph}", f"{ch}", s7, s11)

def R_pm5_21nii(ph, ps, ch, h1, h2, h3):
    s10 = R_pm5_21ni(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    return R_pm2_61i(f"{ps}", f"↔{ph}{ch}", h3, s10)

def R_pm5_21ndd(ph, ps, ch, th, h1, h2, h3):
    s19 = R_con3d(f"{ph}", f"{ch}", f"{ps}", h1)
    s24 = R_con3d(f"{ph}", f"{th}", f"{ps}", h2)
    s27 = R_pm5_21im(f"{ch}", f"{th}")
    s28 = R_syl6c(f"{ph}", f"¬{ps}", f"¬{ch}", f"¬{th}", f"↔{ch}{th}", s19, s24, s27)
    return R_pm2_61d(f"{ph}", f"{ps}", f"↔{ch}{th}", h3, s28)

def R_bija(ph, ps, ch, h1, h2):
    s12 = R_biimpr(f"{ph}", f"{ps}")
    s14 = R_syli(f"{ps}", f"↔{ph}{ps}", f"{ph}", f"{ch}", s12, h1)
    s26 = R_biimp(f"{ph}", f"{ps}")
    s27 = R_con3d(f"↔{ph}{ps}", f"{ph}", f"{ps}", s26)
    s29 = R_syli(f"¬{ps}", f"↔{ph}{ps}", f"¬{ph}", f"{ch}", s27, h2)
    return R_pm2_61d(f"↔{ph}{ps}", f"{ps}", f"{ch}", s14, s29)

@Theorem(2, "pm5.18")
def R_pm5_18(ph, ps):
    s23 = R_pm5_501(f"{ph}", f"¬{ps}")
    s24 = R_con1bid(f"{ph}", f"{ps}", f"↔{ph}¬{ps}", s23)
    s27 = R_pm5_501(f"{ph}", f"{ps}")
    s28 = R_bitr2d(f"{ph}", f"¬↔{ph}¬{ps}", f"{ps}", f"↔{ph}{ps}", s24, s27)
    s40 = R_nbn2(f"{ph}", f"¬{ps}")
    s41 = R_con1bid(f"¬{ph}", f"¬{ps}", f"↔{ph}¬{ps}", s40)
    s44 = R_nbn2(f"{ph}", f"{ps}")
    s45 = R_bitr2d(f"¬{ph}", f"¬↔{ph}¬{ps}", f"¬{ps}", f"↔{ph}{ps}", s41, s44)
    return R_pm2_61i(f"{ph}", f"↔↔{ph}{ps}¬↔{ph}¬{ps}", s28, s45)

@Theorem(2, "xor3")
def R_xor3(ph, ps):
    s14 = R_pm5_18(f"{ph}", f"{ps}")
    s15 = R_con2bii(f"↔{ph}{ps}", f"↔{ph}¬{ps}", s14)
    return R_bicomi(f"↔{ph}¬{ps}", f"¬↔{ph}{ps}", s15)

@Theorem(2, "nbbn")
def R_nbbn(ph, ps):
    s18 = R_xor3(f"{ph}", f"{ps}")
    s21 = R_con2bi(f"{ph}", f"{ps}")
    s24 = R_bicom(f"{ps}", f"¬{ph}")
    return R_3bitrri(f"¬↔{ph}{ps}", f"↔{ph}¬{ps}", f"↔{ps}¬{ph}", f"↔¬{ph}{ps}", s18, s21, s24)

@Theorem(3, "biass")
def R_biass(ph, ps, ch):
    s26 = R_pm5_501(f"{ph}", f"{ps}")
    s27 = R_bibi1d(f"{ph}", f"{ps}", f"↔{ph}{ps}", f"{ch}", s26)
    s30 = R_pm5_501(f"{ph}", f"↔{ps}{ch}")
    s31 = R_bitr3d(f"{ph}", f"↔{ps}{ch}", f"↔↔{ph}{ps}{ch}", f"↔{ph}↔{ps}{ch}", s27, s30)
    s50 = R_nbbn(f"{ps}", f"{ch}")
    s57 = R_nbn2(f"{ph}", f"{ps}")
    s58 = R_bibi1d(f"¬{ph}", f"¬{ps}", f"↔{ph}{ps}", f"{ch}", s57)
    s59 = R_bitr3id(f"¬↔{ps}{ch}", f"↔¬{ps}{ch}", f"¬{ph}", f"↔↔{ph}{ps}{ch}", s50, s58)
    s62 = R_nbn2(f"{ph}", f"↔{ps}{ch}")
    s63 = R_bitr3d(f"¬{ph}", f"¬↔{ps}{ch}", f"↔↔{ph}{ps}{ch}", f"↔{ph}↔{ps}{ch}", s59, s62)
    return R_pm2_61i(f"{ph}", f"↔↔↔{ph}{ps}{ch}↔{ph}↔{ps}{ch}", s31, s63)

@Theorem(3, "biluk")
def R_biluk(ph, ps, ch):
    s41 = R_bicom(f"{ph}", f"{ps}")
    s42 = R_bibi1i(f"↔{ph}{ps}", f"↔{ps}{ph}", f"{ch}", s41)
    s46 = R_biass(f"{ps}", f"{ph}", f"{ch}")
    s47 = R_bitri(f"↔↔{ph}{ps}{ch}", f"↔↔{ps}{ph}{ch}", f"↔{ps}↔{ph}{ch}", s42, s46)
    s51 = R_biass(f"↔{ph}{ps}", f"{ch}", f"↔{ps}↔{ph}{ch}")
    s52 = R_mpbi(f"↔↔↔{ph}{ps}{ch}↔{ps}↔{ph}{ch}", f"↔↔{ph}{ps}↔{ch}↔{ps}↔{ph}{ch}", s47, s51)
    s56 = R_biass(f"{ch}", f"{ps}", f"↔{ph}{ch}")
    return R_bitr4i(f"↔{ph}{ps}", f"↔{ch}↔{ps}↔{ph}{ch}", f"↔↔{ch}{ps}↔{ph}{ch}", s52, s56)

@Theorem(1, "pm5.19")
def R_pm5_19(ph):
    s9 = R_biid(f"{ph}")
    s12 = R_pm5_18(f"{ph}", f"{ph}")
    return R_mpbi(f"↔{ph}{ph}", f"¬↔{ph}¬{ph}", s9, s12)

@Theorem(3, "bi2.04")
def R_bi2_04(ph, ps, ch):
    s13 = R_pm2_04(f"{ph}", f"{ps}", f"{ch}")
    s17 = R_pm2_04(f"{ps}", f"{ph}", f"{ch}")
    return R_impbii(f"→{ph}→{ps}{ch}", f"→{ps}→{ph}{ch}", s13, s17)

@Theorem(2, "pm5.4")
def R_pm5_4(ph, ps):
    s7 = R_pm5_5(f"{ph}", f"{ps}")
    return R_pm5_74i(f"{ph}", f"→{ph}{ps}", f"{ps}", s7)

@Theorem(3, "imdi")
def R_imdi(ph, ps, ch):
    s15 = R_ax_2(f"{ph}", f"{ps}", f"{ch}")
    s19 = R_pm2_86(f"{ph}", f"{ps}", f"{ch}")
    return R_impbii(f"→{ph}→{ps}{ch}", f"→→{ph}{ps}→{ph}{ch}", s15, s19)

@Theorem(3, "pm5.41")
def R_pm5_41(ph, ps, ch):
    s15 = R_imdi(f"{ph}", f"{ps}", f"{ch}")
    return R_bicomi(f"→{ph}→{ps}{ch}", f"→→{ph}{ps}→{ph}{ch}", s15)

@Theorem(3, "imbibi")
def R_imbibi(ph, ps, ch):
    s20 = R_pm5_4(f"{ph}", f"{ps}")
    s24 = R_imbi2(f"→{ph}{ps}", f"{ch}", f"{ph}")
    s25 = R_bitr3id(f"→{ph}{ps}", f"→{ph}→{ph}{ps}", f"↔→{ph}{ps}{ch}", f"→{ph}{ch}", s20, s24)
    return R_pm5_74rd(f"↔→{ph}{ps}{ch}", f"{ph}", f"{ps}", f"{ch}", s25)

@Theorem(1, "pm4.8")
def R_pm4_8(ph):
    s7 = R_pm2_01(f"{ph}")
    s10 = R_ax_1(f"¬{ph}", f"{ph}")
    return R_impbii(f"→{ph}¬{ph}", f"¬{ph}", s7, s10)

@Theorem(1, "pm4.81")
def R_pm4_81(ph):
    s6 = R_pm2_18(f"{ph}")
    s9 = R_pm2_24(f"{ph}", f"{ph}")
    return R_impbii(f"→¬{ph}{ph}", f"{ph}", s6, s9)

@Theorem(4, "imim21b")
def R_imim21b(ph, ps, ch, th):
    s27 = R_bi2_04(f"→{ph}{ch}", f"{ps}", f"{th}")
    s43 = R_pm5_5(f"{ph}", f"{ch}")
    s44 = R_imbi1d(f"{ph}", f"→{ph}{ch}", f"{ch}", f"{th}", s43)
    s45 = R_imim2i(f"{ph}", f"↔→→{ph}{ch}{th}→{ch}{th}", f"{ps}", s44)
    s46 = R_pm5_74d(f"→{ps}{ph}", f"{ps}", f"→→{ph}{ch}{th}", f"→{ch}{th}", s45)
    return R_bitrid(f"→→{ph}{ch}→{ps}{th}", f"→{ps}→→{ph}{ch}{th}", f"→{ps}{ph}", f"→{ps}→{ch}{th}", s27, s46)

@Theorem(2, "pm4.63")
def R_pm4_63(ph, ps):
    s10 = R_df_an(f"{ph}", f"{ps}")
    return R_bicomi(f"∧{ph}{ps}", f"¬→{ph}¬{ps}", s10)

@Theorem(2, "pm4.67")
def R_pm4_67(ph, ps):
    return R_pm4_63(f"¬{ph}", f"{ps}")

@Theorem(2, "imnan")
def R_imnan(ph, ps):
    s9 = R_df_an(f"{ph}", f"{ps}")
    return R_con2bii(f"∧{ph}{ps}", f"→{ph}¬{ps}", s9)

def R_imnani(ph, ps, h1):
    s11 = R_imnan(f"{ph}", f"{ps}")
    return R_mpbir(f"→{ph}¬{ps}", f"¬∧{ph}{ps}", h1, s11)

@Theorem(2, "iman")
def R_iman(ph, ps):
    s18 = R_notnotb(f"{ps}")
    s19 = R_imbi2i(f"{ps}", f"¬¬{ps}", f"{ph}", s18)
    s22 = R_imnan(f"{ph}", f"¬{ps}")
    return R_bitri(f"→{ph}{ps}", f"→{ph}¬¬{ps}", f"¬∧{ph}¬{ps}", s19, s22)

@Theorem(1, "pm3.24")
def R_pm3_24(ph):
    s9 = R_id(f"{ph}")
    s12 = R_iman(f"{ph}", f"{ph}")
    return R_mpbi(f"→{ph}{ph}", f"¬∧{ph}¬{ph}", s9, s12)

@Theorem(2, "annim")
def R_annim(ph, ps):
    s9 = R_iman(f"{ph}", f"{ps}")
    return R_con2bii(f"→{ph}{ps}", f"∧{ph}¬{ps}", s9)

@Theorem(2, "pm4.61")
def R_pm4_61(ph, ps):
    s10 = R_annim(f"{ph}", f"{ps}")
    return R_bicomi(f"∧{ph}¬{ps}", f"¬→{ph}{ps}", s10)

@Theorem(2, "pm4.65")
def R_pm4_65(ph, ps):
    return R_pm4_61(f"¬{ph}", f"{ps}")

def R_imp(ph, ps, ch, h1):
    s11 = R_df_an(f"{ph}", f"{ps}")
    s16 = R_impi(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_sylbi(f"∧{ph}{ps}", f"¬→{ph}¬{ps}", f"{ch}", s11, s16)

def R_impcom(ph, ps, ch, h1):
    s7 = R_com12(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_imp(f"{ps}", f"{ph}", f"{ch}", s7)

def R_con3dimp(ph, ps, ch, h1):
    s9 = R_con3d(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_imp(f"{ph}", f"¬{ch}", f"¬{ps}", s9)

def R_mpnanrd(ph, ps, ch, h1, h2):
    s17 = R_imnan(f"{ps}", f"{ch}")
    s18 = R_sylibr(f"{ph}", f"¬∧{ps}{ch}", f"→{ps}¬{ch}", h2, s17)
    return R_mpd(f"{ph}", f"{ps}", f"¬{ch}", h1, s18)

def R_impd(ph, ps, ch, th, h1):
    s15 = R_com3l(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    s16 = R_imp(f"{ps}", f"{ch}", f"→{ph}{th}", s15)
    return R_com12(f"∧{ps}{ch}", f"{ph}", f"{th}", s16)

def R_impcomd(ph, ps, ch, th, h1):
    s9 = R_com23(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_impd(f"{ph}", f"{ch}", f"{ps}", f"{th}", s9)

def R_ex(ph, ps, ch, h1):
    s14 = R_df_an(f"{ph}", f"{ps}")
    s16 = R_sylbir(f"¬→{ph}¬{ps}", f"∧{ph}{ps}", f"{ch}", s14, h1)
    return R_expi(f"{ph}", f"{ps}", f"{ch}", s16)

def R_expcom(ph, ps, ch, h1):
    s7 = R_ex(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_com12(f"{ph}", f"{ps}", f"{ch}", s7)

def R_expdcom(ph, ps, ch, th, h1):
    s11 = R_com12(f"{ph}", f"∧{ps}{ch}", f"{th}", h1)
    return R_ex(f"{ps}", f"{ch}", f"→{ph}{th}", s11)

def R_expd(ph, ps, ch, th, h1):
    s9 = R_expdcom(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_com3r(f"{ps}", f"{ch}", f"{ph}", f"{th}", s9)

def R_expcomd(ph, ps, ch, th, h1):
    s9 = R_expd(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_com23(f"{ph}", f"{ps}", f"{ch}", f"{th}", s9)

def R_imp31(ph, ps, ch, th, h1):
    s11 = R_imp(f"{ph}", f"{ps}", f"→{ch}{th}", h1)
    return R_imp(f"∧{ph}{ps}", f"{ch}", f"{th}", s11)

def R_imp32(ph, ps, ch, th, h1):
    s10 = R_impd(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_imp(f"{ph}", f"∧{ps}{ch}", f"{th}", s10)

def R_exp31(ph, ps, ch, th, h1):
    s11 = R_ex(f"∧{ph}{ps}", f"{ch}", f"{th}", h1)
    return R_ex(f"{ph}", f"{ps}", f"→{ch}{th}", s11)

def R_exp32(ph, ps, ch, th, h1):
    s10 = R_ex(f"{ph}", f"∧{ps}{ch}", f"{th}", h1)
    return R_expd(f"{ph}", f"{ps}", f"{ch}", f"{th}", s10)

def R_imp4b(ph, ps, ch, th, ta, h1):
    s14 = R_imp(f"{ph}", f"{ps}", f"→{ch}→{th}{ta}", h1)
    return R_impd(f"∧{ph}{ps}", f"{ch}", f"{th}", f"{ta}", s14)

def R_imp4a(ph, ps, ch, th, ta, h1):
    s13 = R_imp4b(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1)
    return R_ex(f"{ph}", f"{ps}", f"→∧{ch}{th}{ta}", s13)

def R_imp4c(ph, ps, ch, th, ta, h1):
    s13 = R_impd(f"{ph}", f"{ps}", f"{ch}", f"→{th}{ta}", h1)
    return R_impd(f"{ph}", f"∧{ps}{ch}", f"{th}", f"{ta}", s13)

def R_imp4d(ph, ps, ch, th, ta, h1):
    s12 = R_imp4a(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1)
    return R_impd(f"{ph}", f"{ps}", f"∧{ch}{th}", f"{ta}", s12)

def R_imp41(ph, ps, ch, th, ta, h1):
    s14 = R_imp(f"{ph}", f"{ps}", f"→{ch}→{th}{ta}", h1)
    return R_imp31(f"∧{ph}{ps}", f"{ch}", f"{th}", f"{ta}", s14)

def R_imp42(ph, ps, ch, th, ta, h1):
    s14 = R_imp32(f"{ph}", f"{ps}", f"{ch}", f"→{th}{ta}", h1)
    return R_imp(f"∧{ph}∧{ps}{ch}", f"{th}", f"{ta}", s14)

def R_imp43(ph, ps, ch, th, ta, h1):
    s13 = R_imp4b(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1)
    return R_imp(f"∧{ph}{ps}", f"∧{ch}{th}", f"{ta}", s13)

def R_imp44(ph, ps, ch, th, ta, h1):
    s13 = R_imp4c(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1)
    return R_imp(f"{ph}", f"∧∧{ps}{ch}{th}", f"{ta}", s13)

def R_imp45(ph, ps, ch, th, ta, h1):
    s13 = R_imp4d(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1)
    return R_imp(f"{ph}", f"∧{ps}∧{ch}{th}", f"{ta}", s13)

def R_exp4b(ph, ps, ch, th, ta, h1):
    s14 = R_expd(f"∧{ph}{ps}", f"{ch}", f"{th}", f"{ta}", h1)
    return R_ex(f"{ph}", f"{ps}", f"→{ch}→{th}{ta}", s14)

def R_exp4a(ph, ps, ch, th, ta, h1):
    s13 = R_imp(f"{ph}", f"{ps}", f"→∧{ch}{th}{ta}", h1)
    return R_exp4b(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", s13)

def R_exp4c(ph, ps, ch, th, ta, h1):
    s13 = R_expd(f"{ph}", f"∧{ps}{ch}", f"{th}", f"{ta}", h1)
    return R_expd(f"{ph}", f"{ps}", f"{ch}", f"→{th}{ta}", s13)

def R_exp4d(ph, ps, ch, th, ta, h1):
    s12 = R_expd(f"{ph}", f"{ps}", f"∧{ch}{th}", f"{ta}", h1)
    return R_exp4a(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", s12)

def R_exp41(ph, ps, ch, th, ta, h1):
    s14 = R_ex(f"∧∧{ph}{ps}{ch}", f"{th}", f"{ta}", h1)
    return R_exp31(f"{ph}", f"{ps}", f"{ch}", f"→{th}{ta}", s14)

def R_exp42(ph, ps, ch, th, ta, h1):
    s13 = R_exp31(f"{ph}", f"∧{ps}{ch}", f"{th}", f"{ta}", h1)
    return R_expd(f"{ph}", f"{ps}", f"{ch}", f"→{th}{ta}", s13)

def R_exp43(ph, ps, ch, th, ta, h1):
    s13 = R_ex(f"∧{ph}{ps}", f"∧{ch}{th}", f"{ta}", h1)
    return R_exp4b(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", s13)

def R_exp44(ph, ps, ch, th, ta, h1):
    s13 = R_exp32(f"{ph}", f"∧{ps}{ch}", f"{th}", f"{ta}", h1)
    return R_expd(f"{ph}", f"{ps}", f"{ch}", f"→{th}{ta}", s13)

def R_exp45(ph, ps, ch, th, ta, h1):
    s12 = R_exp32(f"{ph}", f"{ps}", f"∧{ch}{th}", f"{ta}", h1)
    return R_exp4a(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", s12)

def R_imp5d(ph, ps, ch, th, ta, et, h1):
    s17 = R_imp31(f"{ph}", f"{ps}", f"{ch}", f"→{th}→{ta}{et}", h1)
    return R_impd(f"∧∧{ph}{ps}{ch}", f"{th}", f"{ta}", f"{et}", s17)

def R_imp5a(ph, ps, ch, th, ta, et, h1):
    s15 = R_imp5d(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", f"{et}", h1)
    return R_exp31(f"{ph}", f"{ps}", f"{ch}", f"→∧{th}{ta}{et}", s15)

def R_imp5g(ph, ps, ch, th, ta, et, h1):
    s16 = R_imp4b(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"→{ta}{et}", h1)
    return R_impd(f"∧{ph}{ps}", f"∧{ch}{th}", f"{ta}", f"{et}", s16)

def R_imp55(ph, ps, ch, th, ta, et, h1):
    s15 = R_imp4a(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"→{ta}{et}", h1)
    return R_imp42(f"{ph}", f"{ps}", f"∧{ch}{th}", f"{ta}", f"{et}", s15)

def R_imp511(ph, ps, ch, th, ta, et, h1):
    s15 = R_imp4a(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"→{ta}{et}", h1)
    return R_imp44(f"{ph}", f"{ps}", f"∧{ch}{th}", f"{ta}", f"{et}", s15)

def R_exp5c(ph, ps, ch, th, ta, et, h1):
    s16 = R_exp4a(f"{ph}", f"∧{ps}{ch}", f"{th}", f"{ta}", f"{et}", h1)
    return R_expd(f"{ph}", f"{ps}", f"{ch}", f"→{th}→{ta}{et}", s16)

def R_exp5j(ph, ps, ch, th, ta, et, h1):
    s16 = R_expd(f"{ph}", f"∧∧{ps}{ch}{th}", f"{ta}", f"{et}", h1)
    return R_exp4c(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"→{ta}{et}", s16)

def R_exp5l(ph, ps, ch, th, ta, et, h1):
    s15 = R_expd(f"{ph}", f"∧{ps}{ch}", f"∧{th}{ta}", f"{et}", h1)
    return R_exp5c(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", f"{et}", s15)

def R_exp53(ph, ps, ch, th, ta, et, h1):
    s17 = R_ex(f"∧∧{ph}{ps}∧{ch}{th}", f"{ta}", f"{et}", h1)
    return R_exp43(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"→{ta}{et}", s17)

@Theorem(3, "pm3.3")
def R_pm3_3(ph, ps, ch):
    s10 = R_id(f"→∧{ph}{ps}{ch}")
    return R_expd(f"→∧{ph}{ps}{ch}", f"{ph}", f"{ps}", f"{ch}", s10)

@Theorem(3, "pm3.31")
def R_pm3_31(ph, ps, ch):
    s10 = R_id(f"→{ph}→{ps}{ch}")
    return R_impd(f"→{ph}→{ps}{ch}", f"{ph}", f"{ps}", f"{ch}", s10)

@Theorem(3, "impexp")
def R_impexp(ph, ps, ch):
    s13 = R_pm3_3(f"{ph}", f"{ps}", f"{ch}")
    s17 = R_pm3_31(f"{ph}", f"{ps}", f"{ch}")
    return R_impbii(f"→∧{ph}{ps}{ch}", f"→{ph}→{ps}{ch}", s13, s17)

def R_impancom(ph, ps, ch, th, h1):
    s15 = R_ex(f"{ph}", f"{ps}", f"→{ch}{th}", h1)
    s16 = R_com23(f"{ph}", f"{ps}", f"{ch}", f"{th}", s15)
    return R_imp(f"{ph}", f"{ch}", f"→{ps}{th}", s16)

def R_expdimp(ph, ps, ch, th, h1):
    s10 = R_expd(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_imp(f"{ph}", f"{ps}", f"→{ch}{th}", s10)

def R_expimpd(ph, ps, ch, th, h1):
    s10 = R_ex(f"{ph}", f"{ps}", f"→{ch}{th}", h1)
    return R_impd(f"{ph}", f"{ps}", f"{ch}", f"{th}", s10)

def R_impr(ph, ps, ch, th, h1):
    s10 = R_ex(f"{ph}", f"{ps}", f"→{ch}{th}", h1)
    return R_imp32(f"{ph}", f"{ps}", f"{ch}", f"{th}", s10)

def R_impl(ph, ps, ch, th, h1):
    s9 = R_expd(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_imp31(f"{ph}", f"{ps}", f"{ch}", f"{th}", s9)

def R_expr(ph, ps, ch, th, h1):
    s10 = R_exp32(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_imp(f"{ph}", f"{ps}", f"→{ch}{th}", s10)

def R_expl(ph, ps, ch, th, h1):
    s9 = R_exp31(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_impd(f"{ph}", f"{ps}", f"{ch}", f"{th}", s9)

def R_ancoms(ph, ps, ch, h1):
    s7 = R_expcom(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_imp(f"{ps}", f"{ph}", f"{ch}", s7)

@Theorem(2, "pm3.22")
def R_pm3_22(ph, ps):
    s7 = R_id(f"∧{ps}{ph}")
    return R_ancoms(f"{ps}", f"{ph}", f"∧{ps}{ph}", s7)

@Theorem(2, "ancom")
def R_ancom(ph, ps):
    s8 = R_pm3_22(f"{ph}", f"{ps}")
    s11 = R_pm3_22(f"{ps}", f"{ph}")
    return R_impbii(f"∧{ph}{ps}", f"∧{ps}{ph}", s8, s11)

def R_ancomd(ph, ps, ch, h1):
    s10 = R_ancom(f"{ps}", f"{ch}")
    return R_sylib(f"{ph}", f"∧{ps}{ch}", f"∧{ch}{ps}", h1, s10)

def R_biancomi(ph, ps, ch, h1):
    s10 = R_ancom(f"{ps}", f"{ch}")
    return R_bitr4i(f"{ph}", f"∧{ch}{ps}", f"∧{ps}{ch}", h1, s10)

def R_biancomd(ph, ps, ch, th, h1):
    s11 = R_ancom(f"{th}", f"{ch}")
    return R_bitrdi(f"{ph}", f"{ps}", f"∧{th}{ch}", f"∧{ch}{th}", h1, s11)

@Theorem(3, "ancomst")
def R_ancomst(ph, ps, ch):
    s9 = R_ancom(f"{ph}", f"{ps}")
    return R_imbi1i(f"∧{ph}{ps}", f"∧{ps}{ph}", f"{ch}", s9)

def R_ancomsd(ph, ps, ch, th, h1):
    s9 = R_expcomd(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_impd(f"{ph}", f"{ch}", f"{ps}", f"{th}", s9)

def R_anasss(ph, ps, ch, th, h1):
    s9 = R_exp31(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_imp32(f"{ph}", f"{ps}", f"{ch}", f"{th}", s9)

def R_anassrs(ph, ps, ch, th, h1):
    s9 = R_exp32(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_imp31(f"{ph}", f"{ps}", f"{ch}", f"{th}", s9)

@Theorem(3, "anass")
def R_anass(ph, ps, ch):
    s17 = R_id(f"∧{ph}∧{ps}{ch}")
    s18 = R_anassrs(f"{ph}", f"{ps}", f"{ch}", f"∧{ph}∧{ps}{ch}", s17)
    s24 = R_id(f"∧∧{ph}{ps}{ch}")
    s25 = R_anasss(f"{ph}", f"{ps}", f"{ch}", f"∧∧{ph}{ps}{ch}", s24)
    return R_impbii(f"∧∧{ph}{ps}{ch}", f"∧{ph}∧{ps}{ch}", s18, s25)

@Theorem(2, "pm3.2")
def R_pm3_2(ph, ps):
    s7 = R_id(f"∧{ph}{ps}")
    return R_ex(f"{ph}", f"{ps}", f"∧{ph}{ps}", s7)

def R_pm3_2i(ph, ps, h1, h2):
    s9 = R_pm3_2(f"{ph}", f"{ps}")
    return R_mp2(f"{ph}", f"{ps}", f"∧{ph}{ps}", h1, h2, s9)

@Theorem(2, "pm3.21")
def R_pm3_21(ph, ps):
    s7 = R_id(f"∧{ps}{ph}")
    return R_expcom(f"{ps}", f"{ph}", f"∧{ps}{ph}", s7)

@Theorem(3, "pm3.43i")
def R_pm3_43i(ph, ps, ch):
    s8 = R_pm3_2(f"{ps}", f"{ch}")
    return R_imim3i(f"{ps}", f"{ch}", f"∧{ps}{ch}", f"{ph}", s8)

@Theorem(3, "pm3.43")
def R_pm3_43(ph, ps, ch):
    s14 = R_pm3_43i(f"{ph}", f"{ps}", f"{ch}")
    return R_imp(f"→{ph}{ps}", f"→{ph}{ch}", f"→{ph}∧{ps}{ch}", s14)

@Theorem(2, "dfbi2")
def R_dfbi2(ph, ps):
    s19 = R_dfbi1(f"{ph}", f"{ps}")
    s22 = R_df_an(f"→{ph}{ps}", f"→{ps}{ph}")
    return R_bitr4i(f"↔{ph}{ps}", f"¬→→{ph}{ps}¬→{ps}{ph}", f"∧→{ph}{ps}→{ps}{ph}", s19, s22)

@Theorem(2, "dfbi")
def R_dfbi(ph, ps):
    s22 = R_dfbi2(f"{ph}", f"{ps}")
    s25 = R_dfbi2(f"↔{ph}{ps}", f"∧→{ph}{ps}→{ps}{ph}")
    return R_mpbi(f"↔↔{ph}{ps}∧→{ph}{ps}→{ps}{ph}", f"∧→↔{ph}{ps}∧→{ph}{ps}→{ps}{ph}→∧→{ph}{ps}→{ps}{ph}↔{ph}{ps}", s22, s25)

def R_biimpa(ph, ps, ch, h1):
    s7 = R_biimpd(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_imp(f"{ph}", f"{ps}", f"{ch}", s7)

def R_biimpar(ph, ps, ch, h1):
    s7 = R_biimprd(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_imp(f"{ph}", f"{ch}", f"{ps}", s7)

def R_biimpac(ph, ps, ch, h1):
    s7 = R_biimpcd(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_imp(f"{ps}", f"{ph}", f"{ch}", s7)

def R_biimparc(ph, ps, ch, h1):
    s7 = R_biimprcd(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_imp(f"{ch}", f"{ph}", f"{ps}", s7)

def R_adantr(ph, ps, ch, h1):
    s7 = R_a1d(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_imp(f"{ph}", f"{ch}", f"{ps}", s7)

def R_adantl(ph, ps, ch, h1):
    s7 = R_adantr(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_ancoms(f"{ph}", f"{ch}", f"{ps}", s7)

@Theorem(2, "simpl")
def R_simpl(ph, ps):
    s4 = R_id(f"{ph}")
    return R_adantr(f"{ph}", f"{ph}", f"{ps}", s4)

def R_simpli(ph, ps, h1):
    s7 = R_simpl(f"{ph}", f"{ps}")
    return R_ax_mp(f"∧{ph}{ps}", f"{ph}", h1, s7)

@Theorem(2, "simpr")
def R_simpr(ph, ps):
    s4 = R_id(f"{ps}")
    return R_adantl(f"{ps}", f"{ps}", f"{ph}", s4)

def R_simpri(ph, ps, h1):
    s7 = R_simpr(f"{ph}", f"{ps}")
    return R_ax_mp(f"∧{ph}{ps}", f"{ps}", h1, s7)

def R_intnan(ph, ps, h1):
    s7 = R_simpr(f"{ps}", f"{ph}")
    return R_mto(f"∧{ps}{ph}", f"{ph}", h1, s7)

def R_intnanr(ph, ps, h1):
    s7 = R_simpl(f"{ph}", f"{ps}")
    return R_mto(f"∧{ph}{ps}", f"{ph}", h1, s7)

def R_intnand(ph, ps, ch, h1):
    s8 = R_simpr(f"{ch}", f"{ps}")
    return R_nsyl(f"{ph}", f"{ps}", f"∧{ch}{ps}", h1, s8)

def R_intnanrd(ph, ps, ch, h1):
    s8 = R_simpl(f"{ps}", f"{ch}")
    return R_nsyl(f"{ph}", f"{ps}", f"∧{ps}{ch}", h1, s8)

def R_adantld(ph, ps, ch, th, h1):
    s8 = R_simpr(f"{th}", f"{ps}")
    return R_syl5(f"∧{th}{ps}", f"{ps}", f"{ph}", f"{ch}", s8, h1)

def R_adantrd(ph, ps, ch, th, h1):
    s8 = R_simpl(f"{ps}", f"{th}")
    return R_syl5(f"∧{ps}{th}", f"{ps}", f"{ph}", f"{ch}", s8, h1)

@Theorem(3, "pm3.41")
def R_pm3_41(ph, ps, ch):
    s7 = R_simpl(f"{ph}", f"{ps}")
    return R_imim1i(f"∧{ph}{ps}", f"{ph}", f"{ch}", s7)

@Theorem(3, "pm3.42")
def R_pm3_42(ph, ps, ch):
    s7 = R_simpr(f"{ph}", f"{ps}")
    return R_imim1i(f"∧{ph}{ps}", f"{ps}", f"{ch}", s7)

def R_simpld(ph, ps, ch, h1):
    s8 = R_simpl(f"{ps}", f"{ch}")
    return R_syl(f"{ph}", f"∧{ps}{ch}", f"{ps}", h1, s8)

def R_simprd(ph, ps, ch, h1):
    s7 = R_ancomd(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_simpld(f"{ph}", f"{ch}", f"{ps}", s7)

def R_simprbi(ph, ps, ch, h1):
    s8 = R_biimpi(f"{ph}", f"∧{ps}{ch}", h1)
    return R_simprd(f"{ph}", f"{ps}", f"{ch}", s8)

def R_simplbi(ph, ps, ch, h1):
    s8 = R_biimpi(f"{ph}", f"∧{ps}{ch}", h1)
    return R_simpld(f"{ph}", f"{ps}", f"{ch}", s8)

def R_simprbda(ph, ps, ch, th, h1):
    s11 = R_biimpa(f"{ph}", f"{ps}", f"∧{ch}{th}", h1)
    return R_simpld(f"∧{ph}{ps}", f"{ch}", f"{th}", s11)

def R_simplbda(ph, ps, ch, th, h1):
    s11 = R_biimpa(f"{ph}", f"{ps}", f"∧{ch}{th}", h1)
    return R_simprd(f"∧{ph}{ps}", f"{ch}", f"{th}", s11)

def R_simplbi2(ph, ps, ch, h1):
    s8 = R_biimpri(f"{ph}", f"∧{ps}{ch}", h1)
    return R_ex(f"{ps}", f"{ch}", f"{ph}", s8)

@Theorem(3, "simplbi2comt")
def R_simplbi2comt(ph, ps, ch):
    s11 = R_biimpr(f"{ph}", f"∧{ps}{ch}")
    return R_expcomd(f"↔{ph}∧{ps}{ch}", f"{ps}", f"{ch}", f"{ph}", s11)

def R_simplbi2com(ph, ps, ch, h1):
    s7 = R_simplbi2(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_com12(f"{ps}", f"{ch}", f"{ph}", s7)

def R_simpl2im(ph, ps, ch, th, h1, h2):
    s7 = R_simprd(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_syl(f"{ph}", f"{ch}", f"{th}", s7, h2)

def R_simplbiim(ph, ps, ch, th, h1, h2):
    s7 = R_simprbi(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_syl(f"{ph}", f"{ch}", f"{th}", s7, h2)

def R_impel(ph, ps, ch, th, h1, h2):
    s9 = R_syl5(f"{th}", f"{ps}", f"{ph}", f"{ch}", h2, h1)
    return R_imp(f"{ph}", f"{th}", f"{ch}", s9)

def R_mpan9(ph, ps, ch, th, h1, h2):
    s9 = R_syl5(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2)
    return R_impcom(f"{ch}", f"{ph}", f"{th}", s9)

def R_sylan9(ph, ps, ch, th, ta, h1, h2):
    s12 = R_syl9(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1, h2)
    return R_imp(f"{ph}", f"{th}", f"→{ps}{ta}", s12)

def R_sylan9r(ph, ps, ch, th, ta, h1, h2):
    s12 = R_syl9r(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1, h2)
    return R_imp(f"{th}", f"{ph}", f"→{ps}{ta}", s12)

def R_sylan9bb(ph, ps, ch, th, ta, h1, h2):
    s12 = R_adantr(f"{ph}", f"↔{ps}{ch}", f"{th}", h1)
    s19 = R_adantl(f"{th}", f"↔{ch}{ta}", f"{ph}", h2)
    return R_bitrd(f"∧{ph}{th}", f"{ps}", f"{ch}", f"{ta}", s12, s19)

def R_sylan9bbr(ph, ps, ch, th, ta, h1, h2):
    s12 = R_sylan9bb(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1, h2)
    return R_ancoms(f"{ph}", f"{th}", f"↔{ps}{ta}", s12)

def R_jca(ph, ps, ch, h1, h2):
    s10 = R_pm3_2(f"{ps}", f"{ch}")
    return R_sylc(f"{ph}", f"{ps}", f"{ch}", f"∧{ps}{ch}", h1, h2, s10)

def R_jcad(ph, ps, ch, th, h1, h2):
    s11 = R_pm3_2(f"{ch}", f"{th}")
    return R_syl6c(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"∧{ch}{th}", h1, h2, s11)

def R_jca2(ph, ps, ch, th, h1, h2):
    s10 = R_a1i(f"→{ps}{th}", f"{ph}", h2)
    return R_jcad(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, s10)

def R_jca31(ph, ps, ch, th, h1, h2, h3):
    s10 = R_jca(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    return R_jca(f"{ph}", f"∧{ps}{ch}", f"{th}", s10, h3)

def R_jca32(ph, ps, ch, th, h1, h2, h3):
    s11 = R_jca(f"{ph}", f"{ch}", f"{th}", h2, h3)
    return R_jca(f"{ph}", f"{ps}", f"∧{ch}{th}", h1, s11)

def R_jcai(ph, ps, ch, h1, h2):
    s9 = R_mpd(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    return R_jca(f"{ph}", f"{ps}", f"{ch}", h1, s9)

@Theorem(3, "jcab")
def R_jcab(ph, ps, ch):
    s24 = R_simpl(f"{ps}", f"{ch}")
    s25 = R_imim2i(f"∧{ps}{ch}", f"{ps}", f"{ph}", s24)
    s31 = R_simpr(f"{ps}", f"{ch}")
    s32 = R_imim2i(f"∧{ps}{ch}", f"{ch}", f"{ph}", s31)
    s33 = R_jca(f"→{ph}∧{ps}{ch}", f"→{ph}{ps}", f"→{ph}{ch}", s25, s32)
    s37 = R_pm3_43(f"{ph}", f"{ps}", f"{ch}")
    return R_impbii(f"→{ph}∧{ps}{ch}", f"∧→{ph}{ps}→{ph}{ch}", s33, s37)

@Theorem(3, "pm4.76")
def R_pm4_76(ph, ps, ch):
    s15 = R_jcab(f"{ph}", f"{ps}", f"{ch}")
    return R_bicomi(f"→{ph}∧{ps}{ch}", f"∧→{ph}{ps}→{ph}{ch}", s15)

def R_jctil(ph, ps, ch, h1, h2):
    s6 = R_a1i(f"{ch}", f"{ph}", h2)
    return R_jca(f"{ph}", f"{ch}", f"{ps}", s6, h1)

def R_jctir(ph, ps, ch, h1, h2):
    s7 = R_a1i(f"{ch}", f"{ph}", h2)
    return R_jca(f"{ph}", f"{ps}", f"{ch}", h1, s7)

def R_jccir(ph, ps, ch, h1, h2):
    s9 = R_syl(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    return R_jca(f"{ph}", f"{ps}", f"{ch}", h1, s9)

def R_jccil(ph, ps, ch, h1, h2):
    s8 = R_jccir(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    return R_ancomd(f"{ph}", f"{ps}", f"{ch}", s8)

def R_jctl(ph, ps, h1):
    s4 = R_id(f"{ph}")
    return R_jctil(f"{ph}", f"{ph}", f"{ps}", s4, h1)

def R_jctr(ph, ps, h1):
    s4 = R_id(f"{ph}")
    return R_jctir(f"{ph}", f"{ph}", f"{ps}", s4, h1)

def R_jctild(ph, ps, ch, th, h1, h2):
    s8 = R_a1d(f"{ph}", f"{th}", f"{ps}", h2)
    return R_jcad(f"{ph}", f"{ps}", f"{th}", f"{ch}", s8, h1)

def R_jctird(ph, ps, ch, th, h1, h2):
    s9 = R_a1d(f"{ph}", f"{th}", f"{ps}", h2)
    return R_jcad(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, s9)

@Theorem(2, "iba")
def R_iba(ph, ps):
    s7 = R_pm3_21(f"{ph}", f"{ps}")
    s10 = R_simpl(f"{ps}", f"{ph}")
    return R_impbid1(f"{ph}", f"{ps}", f"∧{ps}{ph}", s7, s10)

@Theorem(2, "ibar")
def R_ibar(ph, ps):
    s6 = R_iba(f"{ph}", f"{ps}")
    return R_biancomd(f"{ph}", f"{ps}", f"{ph}", f"{ps}", s6)

def R_biantru(ph, ps, h1):
    s9 = R_iba(f"{ph}", f"{ps}")
    return R_ax_mp(f"{ph}", f"↔{ps}∧{ps}{ph}", h1, s9)

def R_biantrur(ph, ps, h1):
    s6 = R_biantru(f"{ph}", f"{ps}", h1)
    return R_biancomi(f"{ps}", f"{ph}", f"{ps}", s6)

def R_biantrud(ph, ps, ch, h1):
    s10 = R_iba(f"{ps}", f"{ch}")
    return R_syl(f"{ph}", f"{ps}", f"↔{ch}∧{ch}{ps}", h1, s10)

def R_biantrurd(ph, ps, ch, h1):
    s10 = R_ibar(f"{ps}", f"{ch}")
    return R_syl(f"{ph}", f"{ps}", f"↔{ch}∧{ps}{ch}", h1, s10)

def R_bianfi(ph, ps, h1):
    s8 = R_intnan(f"{ph}", f"{ps}", h1)
    return R_2false(f"{ph}", f"∧{ps}{ph}", h1, s8)

def R_bianfd(ph, ps, ch, h1):
    s10 = R_intnanrd(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_2falsed(f"{ph}", f"{ps}", f"∧{ps}{ch}", h1, s10)

def R_baib(ph, ps, ch, h1):
    s9 = R_ibar(f"{ps}", f"{ch}")
    return R_bitr4id(f"{ps}", f"{ph}", f"∧{ps}{ch}", f"{ch}", h1, s9)

def R_baibr(ph, ps, ch, h1):
    s7 = R_baib(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_bicomd(f"{ps}", f"{ph}", f"{ch}", s7)

def R_rbaibr(ph, ps, ch, h1):
    s7 = R_biancomi(f"{ph}", f"{ch}", f"{ps}", h1)
    return R_baibr(f"{ph}", f"{ch}", f"{ps}", s7)

def R_rbaib(ph, ps, ch, h1):
    s7 = R_rbaibr(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_bicomd(f"{ch}", f"{ps}", f"{ph}", s7)

def R_baibd(ph, ps, ch, th, h1):
    s14 = R_ibar(f"{ch}", f"{th}")
    s15 = R_bicomd(f"{ch}", f"{th}", f"∧{ch}{th}", s14)
    return R_sylan9bb(f"{ph}", f"{ps}", f"∧{ch}{th}", f"{ch}", f"{th}", h1, s15)

def R_rbaibd(ph, ps, ch, th, h1):
    s9 = R_biancomd(f"{ph}", f"{ps}", f"{th}", f"{ch}", h1)
    return R_baibd(f"{ph}", f"{ps}", f"{th}", f"{ch}", s9)

def R_bianabs(ph, ps, ch, h1):
    s9 = R_ibar(f"{ph}", f"{ch}")
    return R_bitr4d(f"{ph}", f"{ps}", f"∧{ph}{ch}", f"{ch}", h1, s9)

@Theorem(3, "pm5.44")
def R_pm5_44(ph, ps, ch):
    s14 = R_jcab(f"{ph}", f"{ps}", f"{ch}")
    return R_baibr(f"→{ph}∧{ps}{ch}", f"→{ph}{ps}", f"→{ph}{ch}", s14)

@Theorem(3, "pm5.42")
def R_pm5_42(ph, ps, ch):
    s16 = R_ibar(f"{ph}", f"{ch}")
    s17 = R_imbi2d(f"{ph}", f"{ch}", f"∧{ph}{ch}", f"{ps}", s16)
    return R_pm5_74i(f"{ph}", f"→{ps}{ch}", f"→{ps}∧{ph}{ch}", s17)

@Theorem(2, "ancl")
def R_ancl(ph, ps):
    s7 = R_pm3_2(f"{ph}", f"{ps}")
    return R_a2i(f"{ph}", f"{ps}", f"∧{ph}{ps}", s7)

@Theorem(2, "anclb")
def R_anclb(ph, ps):
    s7 = R_ibar(f"{ph}", f"{ps}")
    return R_pm5_74i(f"{ph}", f"{ps}", f"∧{ph}{ps}", s7)

@Theorem(2, "ancr")
def R_ancr(ph, ps):
    s7 = R_pm3_21(f"{ph}", f"{ps}")
    return R_a2i(f"{ph}", f"{ps}", f"∧{ps}{ph}", s7)

@Theorem(2, "ancrb")
def R_ancrb(ph, ps):
    s7 = R_iba(f"{ph}", f"{ps}")
    return R_pm5_74i(f"{ph}", f"{ps}", f"∧{ps}{ph}", s7)

def R_ancli(ph, ps, h1):
    s4 = R_id(f"{ph}")
    return R_jca(f"{ph}", f"{ph}", f"{ps}", s4, h1)

def R_ancri(ph, ps, h1):
    s5 = R_id(f"{ph}")
    return R_jca(f"{ph}", f"{ps}", f"{ph}", h1, s5)

def R_ancld(ph, ps, ch, h1):
    s6 = R_idd(f"{ph}", f"{ps}")
    return R_jcad(f"{ph}", f"{ps}", f"{ps}", f"{ch}", s6, h1)

def R_ancrd(ph, ps, ch, h1):
    s7 = R_idd(f"{ph}", f"{ps}")
    return R_jcad(f"{ph}", f"{ps}", f"{ch}", f"{ps}", h1, s7)

def R_impac(ph, ps, ch, h1):
    s9 = R_ancrd(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_imp(f"{ph}", f"{ps}", f"∧{ch}{ps}", s9)

@Theorem(3, "anc2l")
def R_anc2l(ph, ps, ch):
    s15 = R_pm5_42(f"{ph}", f"{ps}", f"{ch}")
    return R_biimpi(f"→{ph}→{ps}{ch}", f"→{ph}→{ps}∧{ph}{ch}", s15)

@Theorem(3, "anc2r")
def R_anc2r(ph, ps, ch):
    s16 = R_pm3_21(f"{ph}", f"{ch}")
    s17 = R_imim2d(f"{ph}", f"{ch}", f"∧{ch}{ph}", f"{ps}", s16)
    return R_a2i(f"{ph}", f"→{ps}{ch}", f"→{ps}∧{ch}{ph}", s17)

def R_anc2li(ph, ps, ch, h1):
    s6 = R_id(f"{ph}")
    return R_jctild(f"{ph}", f"{ps}", f"{ch}", f"{ph}", h1, s6)

def R_anc2ri(ph, ps, ch, h1):
    s6 = R_id(f"{ph}")
    return R_jctird(f"{ph}", f"{ps}", f"{ch}", f"{ph}", h1, s6)

@Theorem(2, "pm4.71")
def R_pm4_71(ph, ps):
    s23 = R_simpl(f"{ph}", f"{ps}")
    s24 = R_biantru(f"→∧{ph}{ps}{ph}", f"→{ph}∧{ph}{ps}", s23)
    s27 = R_anclb(f"{ph}", f"{ps}")
    s30 = R_dfbi2(f"{ph}", f"∧{ph}{ps}")
    return R_3bitr4i(f"→{ph}∧{ph}{ps}", f"∧→{ph}∧{ph}{ps}→∧{ph}{ps}{ph}", f"→{ph}{ps}", f"↔{ph}∧{ph}{ps}", s24, s27, s30)

@Theorem(2, "pm4.71r")
def R_pm4_71r(ph, ps):
    s17 = R_pm4_71(f"{ph}", f"{ps}")
    s23 = R_ancom(f"{ph}", f"{ps}")
    s24 = R_bibi2i(f"∧{ph}{ps}", f"∧{ps}{ph}", f"{ph}", s23)
    return R_bitri(f"→{ph}{ps}", f"↔{ph}∧{ph}{ps}", f"↔{ph}∧{ps}{ph}", s17, s24)

def R_pm4_71i(ph, ps, h1):
    s11 = R_pm4_71(f"{ph}", f"{ps}")
    return R_mpbi(f"→{ph}{ps}", f"↔{ph}∧{ph}{ps}", h1, s11)

def R_pm4_71ri(ph, ps, h1):
    s6 = R_pm4_71i(f"{ph}", f"{ps}", h1)
    return R_biancomi(f"{ph}", f"{ps}", f"{ph}", s6)

def R_pm4_71d(ph, ps, ch, h1):
    s12 = R_pm4_71(f"{ps}", f"{ch}")
    return R_sylib(f"{ph}", f"→{ps}{ch}", f"↔{ps}∧{ps}{ch}", h1, s12)

def R_pm4_71rd(ph, ps, ch, h1):
    s8 = R_pm4_71d(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_biancomd(f"{ph}", f"{ps}", f"{ch}", f"{ps}", s8)

@Theorem(1, "pm4.24")
def R_pm4_24(ph):
    s3 = R_id(f"{ph}")
    return R_pm4_71i(f"{ph}", f"{ph}", s3)

@Theorem(1, "anidm")
def R_anidm(ph):
    s5 = R_pm4_24(f"{ph}")
    return R_bicomi(f"{ph}", f"∧{ph}{ph}", s5)

@Theorem(2, "anidmdbi")
def R_anidmdbi(ph, ps):
    s6 = R_anidm(f"{ps}")
    return R_imbi2i(f"∧{ps}{ps}", f"{ps}", f"{ph}", s6)

def R_anidms(ph, ps, h1):
    s6 = R_ex(f"{ph}", f"{ph}", f"{ps}", h1)
    return R_pm2_43i(f"{ph}", f"{ps}", s6)

@Theorem(3, "imdistan")
def R_imdistan(ph, ps, ch):
    s21 = R_pm5_42(f"{ph}", f"{ps}", f"{ch}")
    s25 = R_impexp(f"{ph}", f"{ps}", f"∧{ph}{ch}")
    return R_bitr4i(f"→{ph}→{ps}{ch}", f"→{ph}→{ps}∧{ph}{ch}", f"→∧{ph}{ps}∧{ph}{ch}", s21, s25)

def R_imdistani(ph, ps, ch, h1):
    s9 = R_anc2li(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_imp(f"{ph}", f"{ps}", f"∧{ph}{ch}", s9)

def R_imdistanri(ph, ps, ch, h1):
    s7 = R_com12(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_impac(f"{ps}", f"{ph}", f"{ch}", s7)

def R_imdistand(ph, ps, ch, th, h1):
    s17 = R_imdistan(f"{ps}", f"{ch}", f"{th}")
    return R_sylib(f"{ph}", f"→{ps}→{ch}{th}", f"→∧{ps}{ch}∧{ps}{th}", h1, s17)

def R_imdistanda(ph, ps, ch, th, h1):
    s10 = R_ex(f"{ph}", f"{ps}", f"→{ch}{th}", h1)
    return R_imdistand(f"{ph}", f"{ps}", f"{ch}", f"{th}", s10)

@Theorem(3, "pm5.3")
def R_pm5_3(ph, ps, ch):
    s13 = R_simpl(f"{ph}", f"{ps}")
    s14 = R_biantrurd(f"∧{ph}{ps}", f"{ph}", f"{ch}", s13)
    return R_pm5_74i(f"∧{ph}{ps}", f"{ch}", f"∧{ph}{ch}", s14)

@Theorem(3, "pm5.32")
def R_pm5_32(ph, ps, ch):
    s50 = R_notbi(f"{ps}", f"{ch}")
    s51 = R_imbi2i(f"↔{ps}{ch}", f"↔¬{ps}¬{ch}", f"{ph}", s50)
    s55 = R_pm5_74(f"{ph}", f"¬{ps}", f"¬{ch}")
    s58 = R_notbi(f"→{ph}¬{ps}", f"→{ph}¬{ch}")
    s59 = R_3bitri(f"→{ph}↔{ps}{ch}", f"→{ph}↔¬{ps}¬{ch}", f"↔→{ph}¬{ps}→{ph}¬{ch}", f"↔¬→{ph}¬{ps}¬→{ph}¬{ch}", s51, s55, s58)
    s66 = R_df_an(f"{ph}", f"{ps}")
    s69 = R_df_an(f"{ph}", f"{ch}")
    s70 = R_bibi12i(f"∧{ph}{ps}", f"¬→{ph}¬{ps}", f"∧{ph}{ch}", f"¬→{ph}¬{ch}", s66, s69)
    return R_bitr4i(f"→{ph}↔{ps}{ch}", f"↔¬→{ph}¬{ps}¬→{ph}¬{ch}", f"↔∧{ph}{ps}∧{ph}{ch}", s59, s70)

def R_pm5_32i(ph, ps, ch, h1):
    s16 = R_pm5_32(f"{ph}", f"{ps}", f"{ch}")
    return R_mpbi(f"→{ph}↔{ps}{ch}", f"↔∧{ph}{ps}∧{ph}{ch}", h1, s16)

def R_pm5_32ri(ph, ps, ch, h1):
    s16 = R_pm5_32i(f"{ph}", f"{ps}", f"{ch}", h1)
    s19 = R_ancom(f"{ps}", f"{ph}")
    s22 = R_ancom(f"{ch}", f"{ph}")
    return R_3bitr4i(f"∧{ph}{ps}", f"∧{ph}{ch}", f"∧{ps}{ph}", f"∧{ch}{ph}", s16, s19, s22)

def R_pm5_32d(ph, ps, ch, th, h1):
    s17 = R_pm5_32(f"{ps}", f"{ch}", f"{th}")
    return R_sylib(f"{ph}", f"→{ps}↔{ch}{th}", f"↔∧{ps}{ch}∧{ps}{th}", h1, s17)

def R_pm5_32rd(ph, ps, ch, th, h1):
    s18 = R_pm5_32d(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    s21 = R_ancom(f"{ch}", f"{ps}")
    s24 = R_ancom(f"{th}", f"{ps}")
    return R_3bitr4g(f"{ph}", f"∧{ps}{ch}", f"∧{ps}{th}", f"∧{ch}{ps}", f"∧{th}{ps}", s18, s21, s24)

def R_pm5_32da(ph, ps, ch, th, h1):
    s10 = R_ex(f"{ph}", f"{ps}", f"↔{ch}{th}", h1)
    return R_pm5_32d(f"{ph}", f"{ps}", f"{ch}", f"{th}", s10)

def R_sylan(ph, ps, ch, th, h1, h2):
    s9 = R_expcom(f"{ps}", f"{ch}", f"{th}", h2)
    return R_mpan9(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, s9)

def R_sylanb(ph, ps, ch, th, h1, h2):
    s7 = R_biimpi(f"{ph}", f"{ps}", h1)
    return R_sylan(f"{ph}", f"{ps}", f"{ch}", f"{th}", s7, h2)

def R_sylanbr(ph, ps, ch, th, h1, h2):
    s7 = R_biimpri(f"{ps}", f"{ph}", h1)
    return R_sylan(f"{ph}", f"{ps}", f"{ch}", f"{th}", s7, h2)

def R_sylanbrc(ph, ps, ch, th, h1, h2, h3):
    s10 = R_jca(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    return R_sylibr(f"{ph}", f"∧{ps}{ch}", f"{th}", s10, h3)

def R_syl2anc(ph, ps, ch, th, h1, h2, h3):
    s10 = R_ex(f"{ps}", f"{ch}", f"{th}", h3)
    return R_sylc(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2, s10)

def R_syl2anc2(ph, ps, ch, th, h1, h2, h3):
    s10 = R_syl(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    return R_syl2anc(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, s10, h3)

def R_sylancl(ph, ps, ch, th, h1, h2, h3):
    s8 = R_a1i(f"{ch}", f"{ph}", h2)
    return R_syl2anc(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, s8, h3)

def R_sylancr(ph, ps, ch, th, h1, h2, h3):
    s7 = R_a1i(f"{ps}", f"{ph}", h1)
    return R_syl2anc(f"{ph}", f"{ps}", f"{ch}", f"{th}", s7, h2, h3)

def R_sylancom(ph, ps, ch, th, h1, h2):
    s9 = R_simpr(f"{ph}", f"{ps}")
    return R_syl2anc(f"∧{ph}{ps}", f"{ch}", f"{ps}", f"{th}", h1, s9, h2)

def R_sylanblc(ph, ps, ch, th, h1, h2, h3):
    s11 = R_biimpi(f"∧{ps}{ch}", f"{th}", h3)
    return R_sylancl(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2, s11)

def R_sylanblrc(ph, ps, ch, th, h1, h2, h3):
    s8 = R_a1i(f"{ch}", f"{ph}", h2)
    return R_sylanbrc(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, s8, h3)

def R_syldan(ph, ps, ch, th, h1, h2):
    s8 = R_simpl(f"{ph}", f"{ps}")
    return R_syl2anc(f"∧{ph}{ps}", f"{ph}", f"{ch}", f"{th}", s8, h1, h2)

def R_sylbida(ph, ps, ch, th, h1, h2):
    s8 = R_biimpa(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_syldan(f"{ph}", f"{ps}", f"{ch}", f"{th}", s8, h2)

def R_sylan2(ph, ps, ch, th, h1, h2):
    s8 = R_adantl(f"{ph}", f"{ch}", f"{ps}", h1)
    return R_syldan(f"{ps}", f"{ph}", f"{ch}", f"{th}", s8, h2)

def R_sylan2b(ph, ps, ch, th, h1, h2):
    s7 = R_biimpi(f"{ph}", f"{ch}", h1)
    return R_sylan2(f"{ph}", f"{ps}", f"{ch}", f"{th}", s7, h2)

def R_sylan2br(ph, ps, ch, th, h1, h2):
    s7 = R_biimpri(f"{ch}", f"{ph}", h1)
    return R_sylan2(f"{ph}", f"{ps}", f"{ch}", f"{th}", s7, h2)

def R_syl2an(ph, ps, ch, th, ta, h1, h2, h3):
    s11 = R_sylan(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h3)
    return R_sylan2(f"{ta}", f"{ph}", f"{ch}", f"{th}", h2, s11)

def R_syl2anr(ph, ps, ch, th, ta, h1, h2, h3):
    s11 = R_syl2an(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1, h2, h3)
    return R_ancoms(f"{ph}", f"{ta}", f"{th}", s11)

def R_syl2anb(ph, ps, ch, th, ta, h1, h2, h3):
    s11 = R_sylanb(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h3)
    return R_sylan2b(f"{ta}", f"{ph}", f"{ch}", f"{th}", h2, s11)

def R_syl2anbr(ph, ps, ch, th, ta, h1, h2, h3):
    s11 = R_sylanbr(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h3)
    return R_sylan2br(f"{ta}", f"{ph}", f"{ch}", f"{th}", h2, s11)

def R_sylancb(ph, ps, ch, th, h1, h2, h3):
    s10 = R_syl2anb(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ph}", h1, h2, h3)
    return R_anidms(f"{ph}", f"{th}", s10)

def R_sylancbr(ph, ps, ch, th, h1, h2, h3):
    s10 = R_syl2anbr(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ph}", h1, h2, h3)
    return R_anidms(f"{ph}", f"{th}", s10)

def R_syldanl(ph, ps, ch, th, ta, h1, h2):
    s15 = R_ex(f"{ph}", f"{ps}", f"{ch}", h1)
    s16 = R_imdistani(f"{ph}", f"{ps}", f"{ch}", s15)
    return R_sylan(f"∧{ph}{ps}", f"∧{ph}{ch}", f"{th}", f"{ta}", s16, h2)

def R_syland(ph, ps, ch, th, ta, h1, h2):
    s16 = R_expd(f"{ph}", f"{ch}", f"{th}", f"{ta}", h2)
    s17 = R_syld(f"{ph}", f"{ps}", f"{ch}", f"→{th}{ta}", h1, s16)
    return R_impd(f"{ph}", f"{ps}", f"{th}", f"{ta}", s17)

def R_sylani(ph, ps, ch, th, ta, h1, h2):
    s10 = R_a1i(f"→{ph}{ch}", f"{ps}", h1)
    return R_syland(f"{ps}", f"{ph}", f"{ch}", f"{th}", f"{ta}", s10, h2)

def R_sylan2d(ph, ps, ch, th, ta, h1, h2):
    s15 = R_ancomsd(f"{ph}", f"{th}", f"{ch}", f"{ta}", h2)
    s16 = R_syland(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1, s15)
    return R_ancomsd(f"{ph}", f"{ps}", f"{th}", f"{ta}", s16)

def R_sylan2i(ph, ps, ch, th, ta, h1, h2):
    s10 = R_a1i(f"→{ph}{th}", f"{ps}", h1)
    return R_sylan2d(f"{ps}", f"{ph}", f"{th}", f"{ch}", f"{ta}", s10, h2)

def R_syl2ani(ph, ps, ch, th, ta, et, h1, h2, h3):
    s13 = R_sylan2i(f"{et}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h2, h3)
    return R_sylani(f"{ph}", f"{ps}", f"{ch}", f"{et}", f"{ta}", h1, s13)

def R_syl2and(ph, ps, ch, th, ta, et, h1, h2, h3):
    s13 = R_sylan2d(f"{ph}", f"{th}", f"{ta}", f"{ch}", f"{et}", h2, h3)
    return R_syland(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{et}", h1, s13)

def R_anim12d(ph, ps, ch, th, ta, h1, h2):
    s13 = R_idd(f"{ph}", f"∧{ch}{ta}")
    return R_syl2and(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", f"∧{ch}{ta}", h1, h2, s13)

def R_anim12d1(ph, ps, ch, th, ta, h1, h2):
    s11 = R_a1i(f"→{th}{ta}", f"{ph}", h2)
    return R_anim12d(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1, s11)

def R_anim1d(ph, ps, ch, th, h1):
    s8 = R_idd(f"{ph}", f"{th}")
    return R_anim12d(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{th}", h1, s8)

def R_anim2d(ph, ps, ch, th, h1):
    s7 = R_idd(f"{ph}", f"{th}")
    return R_anim12d(f"{ph}", f"{th}", f"{th}", f"{ps}", f"{ch}", s7, h1)

def R_anim12i(ph, ps, ch, th, h1, h2):
    s11 = R_id(f"∧{ps}{th}")
    return R_syl2an(f"{ph}", f"{ps}", f"{th}", f"∧{ps}{th}", f"{ch}", h1, h2, s11)

def R_anim12ci(ph, ps, ch, th, h1, h2):
    s11 = R_anim12i(f"{ch}", f"{th}", f"{ph}", f"{ps}", h2, h1)
    return R_ancoms(f"{ch}", f"{ph}", f"∧{th}{ps}", s11)

def R_anim1i(ph, ps, ch, h1):
    s6 = R_id(f"{ch}")
    return R_anim12i(f"{ph}", f"{ps}", f"{ch}", f"{ch}", h1, s6)

def R_anim1ci(ph, ps, ch, h1):
    s6 = R_id(f"{ch}")
    return R_anim12ci(f"{ph}", f"{ps}", f"{ch}", f"{ch}", h1, s6)

def R_anim2i(ph, ps, ch, h1):
    s5 = R_id(f"{ch}")
    return R_anim12i(f"{ch}", f"{ch}", f"{ph}", f"{ps}", s5, h1)

def R_anim12ii(ph, ps, ch, th, ta, h1, h2):
    s18 = R_pm3_43(f"{ps}", f"{ch}", f"{ta}")
    return R_syl2an(f"{ph}", f"→{ps}{ch}", f"→{ps}{ta}", f"→{ps}∧{ch}{ta}", f"{th}", h1, h2, s18)

def R_anim12dan(ph, ps, ch, th, ta, h1, h2):
    s16 = R_ex(f"{ph}", f"{ps}", f"{ch}", h1)
    s21 = R_ex(f"{ph}", f"{th}", f"{ta}", h2)
    s22 = R_anim12d(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", s16, s21)
    return R_imp(f"{ph}", f"∧{ps}{th}", f"∧{ch}{ta}", s22)

def R_im2anan9(ph, ps, ch, th, ta, et, h1, h2):
    s12 = R_adantrd(f"{ph}", f"{ps}", f"{ch}", f"{ta}", h1)
    s18 = R_adantld(f"{th}", f"{ta}", f"{et}", f"{ps}", h2)
    return R_anim12ii(f"{ph}", f"∧{ps}{ta}", f"{ch}", f"{th}", f"{et}", s12, s18)

def R_im2anan9r(ph, ps, ch, th, ta, et, h1, h2):
    s17 = R_im2anan9(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", f"{et}", h1, h2)
    return R_ancoms(f"{ph}", f"{th}", f"→∧{ps}{ta}∧{ch}{et}", s17)

@Theorem(3, "pm3.45")
def R_pm3_45(ph, ps, ch):
    s8 = R_id(f"→{ph}{ps}")
    return R_anim1d(f"→{ph}{ps}", f"{ph}", f"{ps}", f"{ch}", s8)

def R_anbi2i(ph, ps, ch, h1):
    s8 = R_a1i(f"↔{ph}{ps}", f"{ch}", h1)
    return R_pm5_32i(f"{ch}", f"{ph}", f"{ps}", s8)

def R_anbi1i(ph, ps, ch, h1):
    s8 = R_a1i(f"↔{ph}{ps}", f"{ch}", h1)
    return R_pm5_32ri(f"{ch}", f"{ph}", f"{ps}", s8)

def R_anbi2ci(ph, ps, ch, h1):
    s9 = R_anbi1i(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_biancomi(f"∧{ph}{ch}", f"{ch}", f"{ps}", s9)

def R_anbi1ci(ph, ps, ch, h1):
    s9 = R_anbi2i(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_biancomi(f"∧{ch}{ph}", f"{ps}", f"{ch}", s9)

def R_bianbi(ph, ps, ch, th, h1, h2):
    s12 = R_anbi1i(f"{ps}", f"{th}", f"{ch}", h2)
    return R_bitri(f"{ph}", f"∧{ps}{ch}", f"∧{th}{ch}", h1, s12)

def R_anbi12i(ph, ps, ch, th, h1, h2):
    s10 = R_anbi2i(f"{ch}", f"{th}", f"{ph}", h2)
    return R_bianbi(f"∧{ph}{ch}", f"{ph}", f"{th}", f"{ps}", s10, h1)

def R_anbi12ci(ph, ps, ch, th, h1, h2):
    s11 = R_anbi12i(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2)
    return R_biancomi(f"∧{ph}{ch}", f"{th}", f"{ps}", s11)

def R_anbi2d(ph, ps, ch, th, h1):
    s10 = R_a1d(f"{ph}", f"↔{ps}{ch}", f"{th}", h1)
    return R_pm5_32d(f"{ph}", f"{th}", f"{ps}", f"{ch}", s10)

def R_anbi1d(ph, ps, ch, th, h1):
    s10 = R_a1d(f"{ph}", f"↔{ps}{ch}", f"{th}", h1)
    return R_pm5_32rd(f"{ph}", f"{th}", f"{ps}", f"{ch}", s10)

def R_anbi12d(ph, ps, ch, th, ta, h1, h2):
    s15 = R_anbi1d(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    s21 = R_anbi2d(f"{ph}", f"{th}", f"{ta}", f"{ch}", h2)
    return R_bitrd(f"{ph}", f"∧{ps}{th}", f"∧{ch}{th}", f"∧{ch}{ta}", s15, s21)

@Theorem(3, "anbi1")
def R_anbi1(ph, ps, ch):
    s8 = R_id(f"↔{ph}{ps}")
    return R_anbi1d(f"↔{ph}{ps}", f"{ph}", f"{ps}", f"{ch}", s8)

@Theorem(3, "anbi2")
def R_anbi2(ph, ps, ch):
    s8 = R_id(f"↔{ph}{ps}")
    return R_anbi2d(f"↔{ph}{ps}", f"{ph}", f"{ps}", f"{ch}", s8)

def R_anbi1cd(ph, ps, ch, th, h1):
    s11 = R_anbi2d(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_biancomd(f"{ph}", f"∧{th}{ps}", f"{ch}", f"{th}", s11)

@Theorem(4, "an2anr")
def R_an2anr(ph, ps, ch, th):
    s14 = R_ancom(f"{ph}", f"{ps}")
    s17 = R_ancom(f"{ch}", f"{th}")
    return R_anbi12i(f"∧{ph}{ps}", f"∧{ps}{ph}", f"∧{ch}{th}", f"∧{th}{ch}", s14, s17)

@Theorem(4, "pm4.38")
def R_pm4_38(ph, ps, ch, th):
    s15 = R_simpl(f"↔{ph}{ch}", f"↔{ps}{th}")
    s18 = R_simpr(f"↔{ph}{ch}", f"↔{ps}{th}")
    return R_anbi12d(f"∧↔{ph}{ch}↔{ps}{th}", f"{ph}", f"{ch}", f"{ps}", f"{th}", s15, s18)

def R_bi2anan9(ph, ps, ch, th, ta, et, h1, h2):
    s21 = R_pm4_38(f"{ps}", f"{ta}", f"{ch}", f"{et}")
    return R_syl2an(f"{ph}", f"↔{ps}{ch}", f"↔{ta}{et}", f"↔∧{ps}{ta}∧{ch}{et}", f"{th}", h1, h2, s21)

def R_bi2anan9r(ph, ps, ch, th, ta, et, h1, h2):
    s17 = R_bi2anan9(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", f"{et}", h1, h2)
    return R_ancoms(f"{ph}", f"{th}", f"↔∧{ps}{ta}∧{ch}{et}", s17)

def R_bi2bian9(ph, ps, ch, th, ta, et, h1, h2):
    s13 = R_adantr(f"{ph}", f"↔{ps}{ch}", f"{th}", h1)
    s20 = R_adantl(f"{th}", f"↔{ta}{et}", f"{ph}", h2)
    return R_bibi12d(f"∧{ph}{th}", f"{ps}", f"{ch}", f"{ta}", f"{et}", s13, s20)

def R_anbiim(ph, ps, ch, th, h1, h2):
    s11 = R_adantr(f"{ph}", f"→{ch}{th}", f"{ps}", h1)
    s18 = R_adantl(f"{ps}", f"→{th}{ch}", f"{ph}", h2)
    return R_impbid(f"∧{ph}{ps}", f"{ch}", f"{th}", s11, s18)

def R_bianass(ph, ps, ch, th, h1):
    s18 = R_anbi2i(f"{ph}", f"∧{ps}{ch}", f"{th}", h1)
    s22 = R_anass(f"{th}", f"{ps}", f"{ch}")
    return R_bitr4i(f"∧{th}{ph}", f"∧{th}∧{ps}{ch}", f"∧∧{th}{ps}{ch}", s18, s22)

def R_bianassc(ph, ps, ch, th, h1):
    s15 = R_bianass(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    s18 = R_ancom(f"{th}", f"{ps}")
    return R_bianbi(f"∧{th}{ph}", f"∧{th}{ps}", f"{ch}", f"∧{ps}{th}", s15, s18)

@Theorem(3, "an21")
def R_an21(ph, ps, ch):
    s16 = R_biid(f"∧{ph}{ch}")
    s17 = R_bianassc(f"∧{ph}{ch}", f"{ph}", f"{ch}", f"{ps}", s16)
    return R_bicomi(f"∧{ps}∧{ph}{ch}", f"∧∧{ph}{ps}{ch}", s17)

@Theorem(3, "an12")
def R_an12(ph, ps, ch):
    s16 = R_ancom(f"{ps}", f"{ch}")
    s17 = R_bianass(f"∧{ps}{ch}", f"{ch}", f"{ps}", f"{ph}", s16)
    return R_biancomi(f"∧{ph}∧{ps}{ch}", f"{ps}", f"∧{ph}{ch}", s17)

@Theorem(3, "an32")
def R_an32(ph, ps, ch):
    s12 = R_an21(f"{ph}", f"{ps}", f"{ch}")
    return R_biancomi(f"∧∧{ph}{ps}{ch}", f"∧{ph}{ch}", f"{ps}", s12)

@Theorem(3, "an13")
def R_an13(ph, ps, ch):
    s17 = R_an21(f"{ps}", f"{ph}", f"{ch}")
    s20 = R_ancom(f"∧{ps}{ph}", f"{ch}")
    return R_bitr3i(f"∧{ph}∧{ps}{ch}", f"∧∧{ps}{ph}{ch}", f"∧{ch}∧{ps}{ph}", s17, s20)

@Theorem(3, "an31")
def R_an31(ph, ps, ch):
    s23 = R_an13(f"{ph}", f"{ps}", f"{ch}")
    s27 = R_anass(f"{ph}", f"{ps}", f"{ch}")
    s31 = R_anass(f"{ch}", f"{ps}", f"{ph}")
    return R_3bitr4i(f"∧{ph}∧{ps}{ch}", f"∧{ch}∧{ps}{ph}", f"∧∧{ph}{ps}{ch}", f"∧∧{ch}{ps}{ph}", s23, s27, s31)

def R_an12s(ph, ps, ch, th, h1):
    s14 = R_an12(f"{ps}", f"{ph}", f"{ch}")
    return R_sylbi(f"∧{ps}∧{ph}{ch}", f"∧{ph}∧{ps}{ch}", f"{th}", s14, h1)

def R_ancom2s(ph, ps, ch, th, h1):
    s10 = R_pm3_22(f"{ch}", f"{ps}")
    return R_sylan2(f"∧{ch}{ps}", f"{ph}", f"∧{ps}{ch}", f"{th}", s10, h1)

def R_an13s(ph, ps, ch, th, h1):
    s13 = R_exp32(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    s14 = R_com13(f"{ph}", f"{ps}", f"{ch}", f"{th}", s13)
    return R_imp32(f"{ch}", f"{ps}", f"{ph}", f"{th}", s14)

def R_an32s(ph, ps, ch, th, h1):
    s14 = R_an32(f"{ph}", f"{ch}", f"{ps}")
    return R_sylbi(f"∧∧{ph}{ch}{ps}", f"∧∧{ph}{ps}{ch}", f"{th}", s14, h1)

def R_ancom1s(ph, ps, ch, th, h1):
    s10 = R_pm3_22(f"{ps}", f"{ph}")
    return R_sylan(f"∧{ps}{ph}", f"∧{ph}{ps}", f"{ch}", f"{th}", s10, h1)

def R_an31s(ph, ps, ch, th, h1):
    s13 = R_exp31(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    s14 = R_com13(f"{ph}", f"{ps}", f"{ch}", f"{th}", s13)
    return R_imp31(f"{ch}", f"{ps}", f"{ph}", f"{th}", s14)

def R_anass1rs(ph, ps, ch, th, h1):
    s9 = R_anassrs(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_an32s(f"{ph}", f"{ps}", f"{ch}", f"{th}", s9)

@Theorem(4, "an4")
def R_an4(ph, ps, ch, th):
    s25 = R_anass(f"{ph}", f"{ps}", f"∧{ch}{th}")
    s33 = R_an12(f"{ps}", f"{ch}", f"{th}")
    s34 = R_bianass(f"∧{ps}∧{ch}{th}", f"{ch}", f"∧{ps}{th}", f"{ph}", s33)
    return R_bitri(f"∧∧{ph}{ps}∧{ch}{th}", f"∧{ph}∧{ps}∧{ch}{th}", f"∧∧{ph}{ch}∧{ps}{th}", s25, s34)

@Theorem(4, "an42")
def R_an42(ph, ps, ch, th):
    s26 = R_an4(f"{ph}", f"{ps}", f"{ch}", f"{th}")
    s32 = R_ancom(f"{ps}", f"{th}")
    s33 = R_anbi2i(f"∧{ps}{th}", f"∧{th}{ps}", f"∧{ph}{ch}", s32)
    return R_bitri(f"∧∧{ph}{ps}∧{ch}{th}", f"∧∧{ph}{ch}∧{ps}{th}", f"∧∧{ph}{ch}∧{th}{ps}", s26, s33)

@Theorem(4, "an43")
def R_an43(ph, ps, ch, th):
    s18 = R_an42(f"{ph}", f"{th}", f"{ps}", f"{ch}")
    return R_bicomi(f"∧∧{ph}{th}∧{ps}{ch}", f"∧∧{ph}{ps}∧{ch}{th}", s18)

@Theorem(4, "an3")
def R_an3(ph, ps, ch, th):
    s17 = R_an43(f"{ph}", f"{ps}", f"{ch}", f"{th}")
    return R_simplbi(f"∧∧{ph}{ps}∧{ch}{th}", f"∧{ph}{th}", f"∧{ps}{ch}", s17)

def R_an4s(ph, ps, ch, th, ta, h1):
    s19 = R_an4(f"{ph}", f"{ch}", f"{ps}", f"{th}")
    return R_sylbi(f"∧∧{ph}{ch}∧{ps}{th}", f"∧∧{ph}{ps}∧{ch}{th}", f"{ta}", s19, h1)

def R_an42s(ph, ps, ch, th, ta, h1):
    s12 = R_an4s(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1)
    return R_ancom2s(f"∧{ph}{ch}", f"{ps}", f"{th}", f"{ta}", s12)

@Theorem(2, "anabs1")
def R_anabs1(ph, ps):
    s11 = R_simpl(f"{ph}", f"{ps}")
    s12 = R_pm4_71i(f"∧{ph}{ps}", f"{ph}", s11)
    return R_bicomi(f"∧{ph}{ps}", f"∧∧{ph}{ps}{ph}", s12)

@Theorem(2, "anabs5")
def R_anabs5(ph, ps):
    s11 = R_ibar(f"{ph}", f"{ps}")
    s12 = R_bicomd(f"{ph}", f"{ps}", f"∧{ph}{ps}", s11)
    return R_pm5_32i(f"{ph}", f"∧{ph}{ps}", f"{ps}", s12)

@Theorem(2, "anabs7")
def R_anabs7(ph, ps):
    s11 = R_simpr(f"{ph}", f"{ps}")
    s12 = R_pm4_71ri(f"∧{ph}{ps}", f"{ps}", s11)
    return R_bicomi(f"∧{ph}{ps}", f"∧{ps}∧{ph}{ps}", s12)

def R_anabsan(ph, ps, ch, h1):
    s7 = R_pm4_24(f"{ph}")
    return R_sylanb(f"{ph}", f"∧{ph}{ph}", f"{ps}", f"{ch}", s7, h1)

def R_anabss1(ph, ps, ch, h1):
    s8 = R_an32s(f"{ph}", f"{ps}", f"{ph}", f"{ch}", h1)
    return R_anabsan(f"{ph}", f"{ps}", f"{ch}", s8)

def R_anabss4(ph, ps, ch, h1):
    s7 = R_anabss1(f"{ps}", f"{ph}", f"{ch}", h1)
    return R_ancoms(f"{ps}", f"{ph}", f"{ch}", s7)

def R_anabss5(ph, ps, ch, h1):
    s8 = R_anassrs(f"{ph}", f"{ph}", f"{ps}", f"{ch}", h1)
    return R_anabsan(f"{ph}", f"{ps}", f"{ch}", s8)

def R_anabsi5(ph, ps, ch, h1):
    s7 = R_simpl(f"{ph}", f"{ps}")
    return R_mpcom(f"{ph}", f"∧{ph}{ps}", f"{ch}", s7, h1)

def R_anabsi6(ph, ps, ch, h1):
    s8 = R_ancomsd(f"{ph}", f"{ps}", f"{ph}", f"{ch}", h1)
    return R_anabsi5(f"{ph}", f"{ps}", f"{ch}", s8)

def R_anabsi7(ph, ps, ch, h1):
    s7 = R_anabsi6(f"{ps}", f"{ph}", f"{ch}", h1)
    return R_ancoms(f"{ps}", f"{ph}", f"{ch}", s7)

def R_anabsi8(ph, ps, ch, h1):
    s7 = R_anabsi5(f"{ps}", f"{ph}", f"{ch}", h1)
    return R_ancoms(f"{ps}", f"{ph}", f"{ch}", s7)

def R_anabss7(ph, ps, ch, h1):
    s8 = R_anassrs(f"{ps}", f"{ph}", f"{ps}", f"{ch}", h1)
    return R_anabss4(f"{ph}", f"{ps}", f"{ch}", s8)

def R_anabsan2(ph, ps, ch, h1):
    s8 = R_an12s(f"{ph}", f"{ps}", f"{ps}", f"{ch}", h1)
    return R_anabss7(f"{ph}", f"{ps}", f"{ch}", s8)

def R_anabss3(ph, ps, ch, h1):
    s8 = R_anasss(f"{ph}", f"{ps}", f"{ps}", f"{ch}", h1)
    return R_anabsan2(f"{ph}", f"{ps}", f"{ch}", s8)

@Theorem(3, "anandi")
def R_anandi(ph, ps, ch):
    s23 = R_anidm(f"{ph}")
    s24 = R_anbi1i(f"∧{ph}{ph}", f"{ph}", f"∧{ps}{ch}", s23)
    s29 = R_an4(f"{ph}", f"{ph}", f"{ps}", f"{ch}")
    return R_bitr3i(f"∧{ph}∧{ps}{ch}", f"∧∧{ph}{ph}∧{ps}{ch}", f"∧∧{ph}{ps}∧{ph}{ch}", s24, s29)

@Theorem(3, "anandir")
def R_anandir(ph, ps, ch):
    s23 = R_anidm(f"{ch}")
    s24 = R_anbi2i(f"∧{ch}{ch}", f"{ch}", f"∧{ph}{ps}", s23)
    s29 = R_an4(f"{ph}", f"{ps}", f"{ch}", f"{ch}")
    return R_bitr3i(f"∧∧{ph}{ps}{ch}", f"∧∧{ph}{ps}∧{ch}{ch}", f"∧∧{ph}{ch}∧{ps}{ch}", s24, s29)

def R_anandis(ph, ps, ch, th, h1):
    s11 = R_an4s(f"{ph}", f"{ps}", f"{ph}", f"{ch}", f"{th}", h1)
    return R_anabsan(f"{ph}", f"∧{ps}{ch}", f"{th}", s11)

def R_anandirs(ph, ps, ch, th, h1):
    s11 = R_an4s(f"{ph}", f"{ch}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_anabsan2(f"∧{ph}{ps}", f"{ch}", f"{th}", s11)

def R_sylanl1(ph, ps, ch, th, ta, h1, h2):
    s12 = R_anim1i(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_sylan(f"∧{ph}{ch}", f"∧{ps}{ch}", f"{th}", f"{ta}", s12, h2)

def R_sylanl2(ph, ps, ch, th, ta, h1, h2):
    s9 = R_adantl(f"{ph}", f"{ch}", f"{ps}", h1)
    return R_syldanl(f"{ps}", f"{ph}", f"{ch}", f"{th}", f"{ta}", s9, h2)

def R_sylanr1(ph, ps, ch, th, ta, h1, h2):
    s12 = R_anim1i(f"{ph}", f"{ch}", f"{th}", h1)
    return R_sylan2(f"∧{ph}{th}", f"{ps}", f"∧{ch}{th}", f"{ta}", s12, h2)

def R_sylanr2(ph, ps, ch, th, ta, h1, h2):
    s12 = R_anim2i(f"{ph}", f"{th}", f"{ch}", h1)
    return R_sylan2(f"∧{ch}{ph}", f"{ps}", f"∧{ch}{th}", f"{ta}", s12, h2)

def R_syl6an(ph, ps, ch, th, ta, h1, h2, h3):
    s11 = R_ex(f"{ps}", f"{th}", f"{ta}", h3)
    return R_sylsyld(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1, h2, s11)

def R_syl2an2r(ph, ps, ch, th, ta, h1, h2, h3):
    s11 = R_sylan(f"{ph}", f"{ps}", f"{th}", f"{ta}", h1, h3)
    return R_syldan(f"{ph}", f"{ch}", f"{th}", f"{ta}", h2, s11)

def R_syl2an2(ph, ps, ch, th, ta, h1, h2, h3):
    s10 = R_adantl(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_syl2anc(f"∧{ch}{ph}", f"{ps}", f"{th}", f"{ta}", s10, h2, h3)

def R_mpdan(ph, ps, ch, h1, h2):
    s5 = R_id(f"{ph}")
    return R_syl2anc(f"{ph}", f"{ph}", f"{ps}", f"{ch}", s5, h1, h2)

def R_mpancom(ph, ps, ch, h1, h2):
    s6 = R_id(f"{ps}")
    return R_syl2anc(f"{ps}", f"{ph}", f"{ps}", f"{ch}", h1, s6, h2)

def R_mpidan(ph, ps, ch, th, h1, h2):
    s9 = R_adantr(f"{ph}", f"{ch}", f"{ps}", h1)
    return R_mpdan(f"∧{ph}{ps}", f"{ch}", f"{th}", s9, h2)

def R_mpan(ph, ps, ch, h1, h2):
    s6 = R_a1i(f"{ph}", f"{ps}", h1)
    return R_mpancom(f"{ph}", f"{ps}", f"{ch}", s6, h2)

def R_mpan2(ph, ps, ch, h1, h2):
    s6 = R_a1i(f"{ps}", f"{ph}", h1)
    return R_mpdan(f"{ph}", f"{ps}", f"{ch}", s6, h2)

def R_mp2an(ph, ps, ch, h1, h2, h3):
    s8 = R_mpan(f"{ph}", f"{ps}", f"{ch}", h1, h3)
    return R_ax_mp(f"{ps}", f"{ch}", h2, s8)

def R_mp4an(ph, ps, ch, th, ta, h1, h2, h3, h4, h5):
    s11 = R_pm3_2i(f"{ph}", f"{ps}", h1, h2)
    s16 = R_pm3_2i(f"{ch}", f"{th}", h3, h4)
    return R_mp2an(f"∧{ph}{ps}", f"∧{ch}{th}", f"{ta}", s11, s16, h5)

def R_mpan2d(ph, ps, ch, th, h1, h2):
    s10 = R_expd(f"{ph}", f"{ps}", f"{ch}", f"{th}", h2)
    return R_mpid(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, s10)

def R_mpand(ph, ps, ch, th, h1, h2):
    s10 = R_ancomsd(f"{ph}", f"{ps}", f"{ch}", f"{th}", h2)
    return R_mpan2d(f"{ph}", f"{ch}", f"{ps}", f"{th}", h1, s10)

def R_mpani(ph, ps, ch, th, h1, h2):
    s7 = R_a1i(f"{ps}", f"{ph}", h1)
    return R_mpand(f"{ph}", f"{ps}", f"{ch}", f"{th}", s7, h2)

def R_mpan2i(ph, ps, ch, th, h1, h2):
    s7 = R_a1i(f"{ch}", f"{ph}", h1)
    return R_mpan2d(f"{ph}", f"{ps}", f"{ch}", f"{th}", s7, h2)

def R_mp2ani(ph, ps, ch, th, h1, h2, h3):
    s10 = R_mpani(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h3)
    return R_mpi(f"{ph}", f"{ch}", f"{th}", h2, s10)

def R_mp2and(ph, ps, ch, th, h1, h2, h3):
    s10 = R_mpand(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h3)
    return R_mpd(f"{ph}", f"{ch}", f"{th}", h2, s10)

def R_mpanl1(ph, ps, ch, th, h1, h2):
    s9 = R_jctl(f"{ps}", f"{ph}", h1)
    return R_sylan(f"{ps}", f"∧{ph}{ps}", f"{ch}", f"{th}", s9, h2)

def R_mpanl2(ph, ps, ch, th, h1, h2):
    s9 = R_jctr(f"{ph}", f"{ps}", h1)
    return R_sylan(f"{ph}", f"∧{ph}{ps}", f"{ch}", f"{th}", s9, h2)

def R_mpanl12(ph, ps, ch, th, h1, h2, h3):
    s10 = R_mpanl1(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h3)
    return R_mpan(f"{ps}", f"{ch}", f"{th}", h2, s10)

def R_mpanr1(ph, ps, ch, th, h1, h2):
    s10 = R_anassrs(f"{ph}", f"{ps}", f"{ch}", f"{th}", h2)
    return R_mpanl2(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, s10)

def R_mpanr2(ph, ps, ch, th, h1, h2):
    s9 = R_jctr(f"{ps}", f"{ch}", h1)
    return R_sylan2(f"{ps}", f"{ph}", f"∧{ps}{ch}", f"{th}", s9, h2)

def R_mpanr12(ph, ps, ch, th, h1, h2, h3):
    s10 = R_mpanr1(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h3)
    return R_mpan2(f"{ph}", f"{ch}", f"{th}", h2, s10)

def R_mpanlr1(ph, ps, ch, th, ta, h1, h2):
    s10 = R_jctl(f"{ch}", f"{ps}", h1)
    return R_sylanl2(f"{ch}", f"{ph}", f"∧{ps}{ch}", f"{th}", f"{ta}", s10, h2)

def R_mpbirand(ph, ps, ch, th, h1, h2):
    s11 = R_biantrurd(f"{ph}", f"{ch}", f"{th}", h1)
    return R_bitr4d(f"{ph}", f"{ps}", f"∧{ch}{th}", f"{th}", h2, s11)

def R_mpbiran2d(ph, ps, ch, th, h1, h2):
    s10 = R_biancomd(f"{ph}", f"{ps}", f"{th}", f"{ch}", h2)
    return R_mpbirand(f"{ph}", f"{ps}", f"{th}", f"{ch}", h1, s10)

def R_mpbiran(ph, ps, ch, h1, h2):
    s9 = R_biantrur(f"{ps}", f"{ch}", h1)
    return R_bitr4i(f"{ph}", f"∧{ps}{ch}", f"{ch}", h2, s9)

def R_mpbiran2(ph, ps, ch, h1, h2):
    s8 = R_biancomi(f"{ph}", f"{ch}", f"{ps}", h2)
    return R_mpbiran(f"{ph}", f"{ch}", f"{ps}", h1, s8)

def R_mpbir2an(ph, ps, ch, h1, h2, h3):
    s8 = R_mpbiran(f"{ph}", f"{ps}", f"{ch}", h1, h3)
    return R_mpbir(f"{ph}", f"{ch}", h2, s8)

def R_mpbi2and(ph, ps, ch, th, h1, h2, h3):
    s10 = R_jca(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    return R_mpbid(f"{ph}", f"∧{ps}{ch}", f"{th}", s10, h3)

def R_mpbir2and(ph, ps, ch, th, h1, h2, h3):
    s10 = R_jca(f"{ph}", f"{ch}", f"{th}", h1, h2)
    return R_mpbird(f"{ph}", f"{ps}", f"∧{ch}{th}", s10, h3)

def R_adantll(ph, ps, ch, th, h1):
    s8 = R_simpr(f"{th}", f"{ph}")
    return R_sylan(f"∧{th}{ph}", f"{ph}", f"{ps}", f"{ch}", s8, h1)

def R_adantlr(ph, ps, ch, th, h1):
    s8 = R_simpl(f"{ph}", f"{th}")
    return R_sylan(f"∧{ph}{th}", f"{ph}", f"{ps}", f"{ch}", s8, h1)

def R_adantrl(ph, ps, ch, th, h1):
    s8 = R_simpr(f"{th}", f"{ps}")
    return R_sylan2(f"∧{th}{ps}", f"{ph}", f"{ps}", f"{ch}", s8, h1)

def R_adantrr(ph, ps, ch, th, h1):
    s8 = R_simpl(f"{ps}", f"{th}")
    return R_sylan2(f"∧{ps}{th}", f"{ph}", f"{ps}", f"{ch}", s8, h1)

def R_adantlll(ph, ps, ch, th, ta, h1):
    s9 = R_simpr(f"{ta}", f"{ph}")
    return R_sylanl1(f"∧{ta}{ph}", f"{ph}", f"{ps}", f"{ch}", f"{th}", s9, h1)

def R_adantllr(ph, ps, ch, th, ta, h1):
    s9 = R_simpl(f"{ph}", f"{ta}")
    return R_sylanl1(f"∧{ph}{ta}", f"{ph}", f"{ps}", f"{ch}", f"{th}", s9, h1)

def R_adantlrl(ph, ps, ch, th, ta, h1):
    s9 = R_simpr(f"{ta}", f"{ps}")
    return R_sylanl2(f"∧{ta}{ps}", f"{ph}", f"{ps}", f"{ch}", f"{th}", s9, h1)

def R_adantlrr(ph, ps, ch, th, ta, h1):
    s9 = R_simpl(f"{ps}", f"{ta}")
    return R_sylanl2(f"∧{ps}{ta}", f"{ph}", f"{ps}", f"{ch}", f"{th}", s9, h1)

def R_adantrll(ph, ps, ch, th, ta, h1):
    s9 = R_simpr(f"{ta}", f"{ps}")
    return R_sylanr1(f"∧{ta}{ps}", f"{ph}", f"{ps}", f"{ch}", f"{th}", s9, h1)

def R_adantrlr(ph, ps, ch, th, ta, h1):
    s9 = R_simpl(f"{ps}", f"{ta}")
    return R_sylanr1(f"∧{ps}{ta}", f"{ph}", f"{ps}", f"{ch}", f"{th}", s9, h1)

def R_adantrrl(ph, ps, ch, th, ta, h1):
    s9 = R_simpr(f"{ta}", f"{ch}")
    return R_sylanr2(f"∧{ta}{ch}", f"{ph}", f"{ps}", f"{ch}", f"{th}", s9, h1)

def R_adantrrr(ph, ps, ch, th, ta, h1):
    s9 = R_simpl(f"{ch}", f"{ta}")
    return R_sylanr2(f"∧{ch}{ta}", f"{ph}", f"{ps}", f"{ch}", f"{th}", s9, h1)

def R_ad2antrr(ph, ps, ch, th, h1):
    s8 = R_adantr(f"{ph}", f"{ps}", f"{th}", h1)
    return R_adantlr(f"{ph}", f"{th}", f"{ps}", f"{ch}", s8)

def R_ad2antlr(ph, ps, ch, th, h1):
    s8 = R_adantr(f"{ph}", f"{ps}", f"{th}", h1)
    return R_adantll(f"{ph}", f"{th}", f"{ps}", f"{ch}", s8)

def R_ad2antrl(ph, ps, ch, th, h1):
    s8 = R_adantl(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_adantrr(f"{ch}", f"{ph}", f"{ps}", f"{th}", s8)

def R_ad2antll(ph, ps, ch, th, h1):
    s9 = R_adantl(f"{ph}", f"{ps}", f"{th}", h1)
    return R_adantl(f"∧{th}{ph}", f"{ps}", f"{ch}", s9)

def R_ad3antrrr(ph, ps, ch, th, ta, h1):
    s10 = R_adantr(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_ad2antrr(f"∧{ph}{ch}", f"{ps}", f"{th}", f"{ta}", s10)

def R_ad3antlr(ph, ps, ch, th, ta, h1):
    s10 = R_adantl(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_ad2antrr(f"∧{ch}{ph}", f"{ps}", f"{th}", f"{ta}", s10)

def R_ad4antr(ph, ps, ch, th, ta, et, h1):
    s11 = R_adantr(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_ad3antrrr(f"∧{ph}{ch}", f"{ps}", f"{th}", f"{ta}", f"{et}", s11)

def R_ad4antlr(ph, ps, ch, th, ta, et, h1):
    s11 = R_adantl(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_ad3antrrr(f"∧{ch}{ph}", f"{ps}", f"{th}", f"{ta}", f"{et}", s11)

def R_ad5antr(ph, ps, ch, th, ta, et, ze, h1):
    s12 = R_adantr(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_ad4antr(f"∧{ph}{ch}", f"{ps}", f"{th}", f"{ta}", f"{et}", f"{ze}", s12)

def R_ad5antlr(ph, ps, ch, th, ta, et, ze, h1):
    s12 = R_adantl(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_ad4antr(f"∧{ch}{ph}", f"{ps}", f"{th}", f"{ta}", f"{et}", f"{ze}", s12)

def R_ad6antr(ph, ps, ch, th, ta, et, ze, si, h1):
    s13 = R_adantr(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_ad5antr(f"∧{ph}{ch}", f"{ps}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"{si}", s13)

def R_ad6antlr(ph, ps, ch, th, ta, et, ze, si, h1):
    s13 = R_adantl(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_ad5antr(f"∧{ch}{ph}", f"{ps}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"{si}", s13)

def R_ad7antr(ph, ps, ch, th, ta, et, ze, si, rh, h1):
    s14 = R_adantr(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_ad6antr(f"∧{ph}{ch}", f"{ps}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"{si}", f"{rh}", s14)

def R_ad7antlr(ph, ps, ch, th, ta, et, ze, si, rh, h1):
    s14 = R_adantl(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_ad6antr(f"∧{ch}{ph}", f"{ps}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"{si}", f"{rh}", s14)

def R_ad8antr(ph, ps, ch, th, ta, et, ze, si, rh, mu, h1):
    s15 = R_adantr(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_ad7antr(f"∧{ph}{ch}", f"{ps}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"{si}", f"{rh}", f"{mu}", s15)

def R_ad8antlr(ph, ps, ch, th, ta, et, ze, si, rh, mu, h1):
    s15 = R_adantl(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_ad7antr(f"∧{ch}{ph}", f"{ps}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"{si}", f"{rh}", f"{mu}", s15)

def R_ad9antr(ph, ps, ch, th, ta, et, ze, si, rh, mu, la, h1):
    s16 = R_adantr(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_ad8antr(f"∧{ph}{ch}", f"{ps}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"{si}", f"{rh}", f"{mu}", f"{la}", s16)

def R_ad9antlr(ph, ps, ch, th, ta, et, ze, si, rh, mu, la, h1):
    s16 = R_adantl(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_ad8antr(f"∧{ch}{ph}", f"{ps}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"{si}", f"{rh}", f"{mu}", f"{la}", s16)

def R_ad10antr(ph, ps, ch, th, ta, et, ze, si, rh, mu, la, ka, h1):
    s17 = R_adantr(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_ad9antr(f"∧{ph}{ch}", f"{ps}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"{si}", f"{rh}", f"{mu}", f"{la}", f"{ka}", s17)

def R_ad10antlr(ph, ps, ch, th, ta, et, ze, si, rh, mu, la, ka, h1):
    s17 = R_adantl(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_ad9antr(f"∧{ch}{ph}", f"{ps}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"{si}", f"{rh}", f"{mu}", f"{la}", f"{ka}", s17)

def R_ad2ant2l(ph, ps, ch, th, ta, h1):
    s11 = R_adantrl(f"{ph}", f"{ps}", f"{ch}", f"{ta}", h1)
    return R_adantll(f"{ph}", f"∧{ta}{ps}", f"{ch}", f"{th}", s11)

def R_ad2ant2r(ph, ps, ch, th, ta, h1):
    s11 = R_adantrr(f"{ph}", f"{ps}", f"{ch}", f"{ta}", h1)
    return R_adantlr(f"{ph}", f"∧{ps}{ta}", f"{ch}", f"{th}", s11)

def R_ad2ant2lr(ph, ps, ch, th, ta, h1):
    s11 = R_adantrr(f"{ph}", f"{ps}", f"{ch}", f"{ta}", h1)
    return R_adantll(f"{ph}", f"∧{ps}{ta}", f"{ch}", f"{th}", s11)

def R_ad2ant2rl(ph, ps, ch, th, ta, h1):
    s11 = R_adantrl(f"{ph}", f"{ps}", f"{ch}", f"{ta}", h1)
    return R_adantlr(f"{ph}", f"∧{ta}{ps}", f"{ch}", f"{th}", s11)

def R_adantl3r(ph, ps, ch, th, ta, et, h1):
    s17 = R_id(f"∧{ph}{ps}")
    s18 = R_adantlr(f"{ph}", f"{ps}", f"∧{ph}{ps}", f"{et}", s17)
    return R_sylanl1(f"∧∧{ph}{et}{ps}", f"∧{ph}{ps}", f"{ch}", f"{th}", f"{ta}", s18, h1)

def R_ad4ant13(ph, ps, ch, th, ta, h1):
    s11 = R_adantr(f"∧{ph}{ps}", f"{ch}", f"{ta}", h1)
    return R_adantllr(f"{ph}", f"{ps}", f"{ta}", f"{ch}", f"{th}", s11)

def R_ad4ant14(ph, ps, ch, th, ta, h1):
    s11 = R_adantlr(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_adantlr(f"∧{ph}{th}", f"{ps}", f"{ch}", f"{ta}", s11)

def R_ad4ant23(ph, ps, ch, th, ta, h1):
    s11 = R_adantr(f"∧{ph}{ps}", f"{ch}", f"{ta}", h1)
    return R_adantlll(f"{ph}", f"{ps}", f"{ta}", f"{ch}", f"{th}", s11)

def R_ad4ant24(ph, ps, ch, th, ta, h1):
    s10 = R_adantlr(f"{ph}", f"{ps}", f"{ch}", f"{ta}", h1)
    return R_adantlll(f"{ph}", f"{ta}", f"{ps}", f"{ch}", f"{th}", s10)

def R_adantl4r(ph, ps, ch, th, ta, et, ze, h1):
    s29 = R_ex(f"∧∧∧{ph}{ch}{th}{ta}", f"{et}", f"{ze}", h1)
    s30 = R_adantl3r(f"{ph}", f"{ch}", f"{th}", f"{ta}", f"→{et}{ze}", f"{ps}", s29)
    return R_imp(f"∧∧∧∧{ph}{ps}{ch}{th}{ta}", f"{et}", f"{ze}", s30)

def R_ad5ant12(ph, ps, ch, th, ta, et, h1):
    return R_ad3antrrr(f"∧{ph}{ps}", f"{ch}", f"{th}", f"{ta}", f"{et}", h1)

def R_ad5ant13(ph, ps, ch, th, ta, et, h1):
    s13 = R_adantlr(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_ad2antrr(f"∧∧{ph}{th}{ps}", f"{ch}", f"{ta}", f"{et}", s13)

def R_ad5ant14(ph, ps, ch, th, ta, et, h1):
    s12 = R_adantlr(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_ad4ant13(f"∧{ph}{th}", f"{ps}", f"{ch}", f"{ta}", f"{et}", s12)

def R_ad5ant15(ph, ps, ch, th, ta, et, h1):
    s12 = R_adantlr(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_ad4ant14(f"∧{ph}{th}", f"{ps}", f"{ch}", f"{ta}", f"{et}", s12)

def R_ad5ant23(ph, ps, ch, th, ta, et, h1):
    s13 = R_adantll(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_ad2antrr(f"∧∧{th}{ph}{ps}", f"{ch}", f"{ta}", f"{et}", s13)

def R_ad5ant24(ph, ps, ch, th, ta, et, h1):
    s12 = R_adantll(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_ad4ant13(f"∧{th}{ph}", f"{ps}", f"{ch}", f"{ta}", f"{et}", s12)

def R_ad5ant25(ph, ps, ch, th, ta, et, h1):
    s12 = R_adantll(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    return R_ad4ant14(f"∧{th}{ph}", f"{ps}", f"{ch}", f"{ta}", f"{et}", s12)

def R_adantl5r(ph, ps, ch, th, ta, et, ze, si, h1):
    s34 = R_ex(f"∧∧∧∧{ph}{ch}{th}{ta}{et}", f"{ze}", f"{si}", h1)
    s35 = R_adantl4r(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", f"{et}", f"→{ze}{si}", s34)
    return R_imp(f"∧∧∧∧∧{ph}{ps}{ch}{th}{ta}{et}", f"{ze}", f"{si}", s35)

def R_adantl6r(ph, ps, ch, th, ta, et, ze, si, rh, h1):
    s39 = R_ex(f"∧∧∧∧∧{ph}{ch}{th}{ta}{et}{ze}", f"{si}", f"{rh}", h1)
    s40 = R_adantl5r(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"→{si}{rh}", s39)
    return R_imp(f"∧∧∧∧∧∧{ph}{ps}{ch}{th}{ta}{et}{ze}", f"{si}", f"{rh}", s40)

@Theorem(3, "pm3.33")
def R_pm3_33(ph, ps, ch):
    s12 = R_imim1(f"{ph}", f"{ps}", f"{ch}")
    return R_imp(f"→{ph}{ps}", f"→{ps}{ch}", f"→{ph}{ch}", s12)

@Theorem(3, "pm3.34")
def R_pm3_34(ph, ps, ch):
    s12 = R_imim2(f"{ps}", f"{ch}", f"{ph}")
    return R_imp(f"→{ps}{ch}", f"→{ph}{ps}", f"→{ph}{ch}", s12)

@Theorem(3, "simpll")
def R_simpll(ph, ps, ch):
    s5 = R_id(f"{ph}")
    return R_ad2antrr(f"{ph}", f"{ph}", f"{ps}", f"{ch}", s5)

def R_simplld(ph, ps, ch, th, h1):
    s9 = R_simpld(f"{ph}", f"∧{ps}{ch}", f"{th}", h1)
    return R_simpld(f"{ph}", f"{ps}", f"{ch}", s9)

@Theorem(3, "simplr")
def R_simplr(ph, ps, ch):
    s5 = R_id(f"{ps}")
    return R_ad2antlr(f"{ps}", f"{ps}", f"{ph}", f"{ch}", s5)

def R_simplrd(ph, ps, ch, th, h1):
    s9 = R_simpld(f"{ph}", f"∧{ps}{ch}", f"{th}", h1)
    return R_simprd(f"{ph}", f"{ps}", f"{ch}", s9)

@Theorem(3, "simprl")
def R_simprl(ph, ps, ch):
    s5 = R_id(f"{ps}")
    return R_ad2antrl(f"{ps}", f"{ps}", f"{ph}", f"{ch}", s5)

def R_simprld(ph, ps, ch, th, h1):
    s9 = R_simprd(f"{ph}", f"{ps}", f"∧{ch}{th}", h1)
    return R_simpld(f"{ph}", f"{ch}", f"{th}", s9)

@Theorem(3, "simprr")
def R_simprr(ph, ps, ch):
    s5 = R_id(f"{ch}")
    return R_ad2antll(f"{ch}", f"{ch}", f"{ph}", f"{ps}", s5)

def R_simprrd(ph, ps, ch, th, h1):
    s9 = R_simprd(f"{ph}", f"{ps}", f"∧{ch}{th}", h1)
    return R_simprd(f"{ph}", f"{ch}", f"{th}", s9)

@Theorem(4, "simplll")
def R_simplll(ph, ps, ch, th):
    s6 = R_id(f"{ph}")
    return R_ad3antrrr(f"{ph}", f"{ph}", f"{ps}", f"{ch}", f"{th}", s6)

@Theorem(4, "simpllr")
def R_simpllr(ph, ps, ch, th):
    s6 = R_id(f"{ps}")
    return R_ad3antlr(f"{ps}", f"{ps}", f"{ph}", f"{ch}", f"{th}", s6)

@Theorem(4, "simplrl")
def R_simplrl(ph, ps, ch, th):
    s8 = R_simpl(f"{ps}", f"{ch}")
    return R_ad2antlr(f"∧{ps}{ch}", f"{ps}", f"{ph}", f"{th}", s8)

@Theorem(4, "simplrr")
def R_simplrr(ph, ps, ch, th):
    s8 = R_simpr(f"{ps}", f"{ch}")
    return R_ad2antlr(f"∧{ps}{ch}", f"{ch}", f"{ph}", f"{th}", s8)

@Theorem(4, "simprll")
def R_simprll(ph, ps, ch, th):
    s8 = R_simpl(f"{ps}", f"{ch}")
    return R_ad2antrl(f"∧{ps}{ch}", f"{ps}", f"{ph}", f"{th}", s8)

@Theorem(4, "simprlr")
def R_simprlr(ph, ps, ch, th):
    s8 = R_simpr(f"{ps}", f"{ch}")
    return R_ad2antrl(f"∧{ps}{ch}", f"{ch}", f"{ph}", f"{th}", s8)

@Theorem(4, "simprrl")
def R_simprrl(ph, ps, ch, th):
    s8 = R_simpl(f"{ch}", f"{th}")
    return R_ad2antll(f"∧{ch}{th}", f"{ch}", f"{ph}", f"{ps}", s8)

@Theorem(4, "simprrr")
def R_simprrr(ph, ps, ch, th):
    s8 = R_simpr(f"{ch}", f"{th}")
    return R_ad2antll(f"∧{ch}{th}", f"{th}", f"{ph}", f"{ps}", s8)

@Theorem(5, "simp-4l")
def R_simp_4l(ph, ps, ch, th, ta):
    s7 = R_id(f"{ph}")
    return R_ad4antr(f"{ph}", f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", s7)

@Theorem(5, "simp-4r")
def R_simp_4r(ph, ps, ch, th, ta):
    s7 = R_id(f"{ps}")
    return R_ad4antlr(f"{ps}", f"{ps}", f"{ph}", f"{ch}", f"{th}", f"{ta}", s7)

@Theorem(6, "simp-5l")
def R_simp_5l(ph, ps, ch, th, ta, et):
    s8 = R_id(f"{ph}")
    return R_ad5antr(f"{ph}", f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", f"{et}", s8)

@Theorem(6, "simp-5r")
def R_simp_5r(ph, ps, ch, th, ta, et):
    s8 = R_id(f"{ps}")
    return R_ad5antlr(f"{ps}", f"{ps}", f"{ph}", f"{ch}", f"{th}", f"{ta}", f"{et}", s8)

@Theorem(7, "simp-6l")
def R_simp_6l(ph, ps, ch, th, ta, et, ze):
    s9 = R_id(f"{ph}")
    return R_ad6antr(f"{ph}", f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", f"{et}", f"{ze}", s9)

@Theorem(7, "simp-6r")
def R_simp_6r(ph, ps, ch, th, ta, et, ze):
    s9 = R_id(f"{ps}")
    return R_ad6antlr(f"{ps}", f"{ps}", f"{ph}", f"{ch}", f"{th}", f"{ta}", f"{et}", f"{ze}", s9)

@Theorem(8, "simp-7l")
def R_simp_7l(ph, ps, ch, th, ta, et, ze, si):
    s10 = R_id(f"{ph}")
    return R_ad7antr(f"{ph}", f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"{si}", s10)

@Theorem(8, "simp-7r")
def R_simp_7r(ph, ps, ch, th, ta, et, ze, si):
    s10 = R_id(f"{ps}")
    return R_ad7antlr(f"{ps}", f"{ps}", f"{ph}", f"{ch}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"{si}", s10)

@Theorem(9, "simp-8l")
def R_simp_8l(ph, ps, ch, th, ta, et, ze, si, rh):
    s11 = R_id(f"{ph}")
    return R_ad8antr(f"{ph}", f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"{si}", f"{rh}", s11)

@Theorem(9, "simp-8r")
def R_simp_8r(ph, ps, ch, th, ta, et, ze, si, rh):
    s11 = R_id(f"{ps}")
    return R_ad8antlr(f"{ps}", f"{ps}", f"{ph}", f"{ch}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"{si}", f"{rh}", s11)

@Theorem(10, "simp-9l")
def R_simp_9l(ph, ps, ch, th, ta, et, ze, si, rh, mu):
    s12 = R_id(f"{ph}")
    return R_ad9antr(f"{ph}", f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"{si}", f"{rh}", f"{mu}", s12)

@Theorem(10, "simp-9r")
def R_simp_9r(ph, ps, ch, th, ta, et, ze, si, rh, mu):
    s12 = R_id(f"{ps}")
    return R_ad9antlr(f"{ps}", f"{ps}", f"{ph}", f"{ch}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"{si}", f"{rh}", f"{mu}", s12)

@Theorem(11, "simp-10l")
def R_simp_10l(ph, ps, ch, th, ta, et, ze, si, rh, mu, la):
    s13 = R_id(f"{ph}")
    return R_ad10antr(f"{ph}", f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"{si}", f"{rh}", f"{mu}", f"{la}", s13)

@Theorem(11, "simp-10r")
def R_simp_10r(ph, ps, ch, th, ta, et, ze, si, rh, mu, la):
    s13 = R_id(f"{ps}")
    return R_ad10antlr(f"{ps}", f"{ps}", f"{ph}", f"{ch}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"{si}", f"{rh}", f"{mu}", f"{la}", s13)

@Theorem(12, "simp-11l")
def R_simp_11l(ph, ps, ch, th, ta, et, ze, si, rh, mu, la, ka):
    s16 = R_simpl(f"{ph}", f"{ps}")
    return R_ad10antr(f"∧{ph}{ps}", f"{ph}", f"{ch}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"{si}", f"{rh}", f"{mu}", f"{la}", f"{ka}", s16)

@Theorem(12, "simp-11r")
def R_simp_11r(ph, ps, ch, th, ta, et, ze, si, rh, mu, la, ka):
    s16 = R_simpr(f"{ph}", f"{ps}")
    return R_ad10antr(f"∧{ph}{ps}", f"{ps}", f"{ch}", f"{th}", f"{ta}", f"{et}", f"{ze}", f"{si}", f"{rh}", f"{mu}", f"{la}", f"{ka}", s16)

def R_pm2_01da(ph, ps, h1):
    s7 = R_ex(f"{ph}", f"{ps}", f"¬{ps}", h1)
    return R_pm2_01d(f"{ph}", f"{ps}", s7)

def R_pm2_18da(ph, ps, h1):
    s7 = R_ex(f"{ph}", f"¬{ps}", f"{ps}", h1)
    return R_pm2_18d(f"{ph}", f"{ps}", s7)

def R_impbida(ph, ps, ch, h1, h2):
    s7 = R_ex(f"{ph}", f"{ps}", f"{ch}", h1)
    s12 = R_ex(f"{ph}", f"{ch}", f"{ps}", h2)
    return R_impbid(f"{ph}", f"{ps}", f"{ch}", s7, s12)

def R_pm5_21nd(ph, ps, ch, th, h1, h2, h3):
    s8 = R_ex(f"{ph}", f"{ps}", f"{th}", h1)
    s13 = R_ex(f"{ph}", f"{ch}", f"{th}", h2)
    s21 = R_a1i(f"→{th}↔{ps}{ch}", f"{ph}", h3)
    return R_pm5_21ndd(f"{ph}", f"{th}", f"{ps}", f"{ch}", s8, s13, s21)

@Theorem(2, "pm3.35")
def R_pm3_35(ph, ps):
    s7 = R_pm2_27(f"{ph}", f"{ps}")
    return R_imp(f"{ph}", f"→{ph}{ps}", f"{ps}", s7)

def R_pm5_74da(ph, ps, ch, th, h1):
    s10 = R_ex(f"{ph}", f"{ps}", f"↔{ch}{th}", h1)
    return R_pm5_74d(f"{ph}", f"{ps}", f"{ch}", f"{th}", s10)

@Theorem(3, "bitr")
def R_bitr(ph, ps, ch):
    s12 = R_bibi1(f"{ph}", f"{ps}", f"{ch}")
    return R_biimpar(f"↔{ph}{ps}", f"↔{ph}{ch}", f"↔{ps}{ch}", s12)

@Theorem(3, "biantr")
def R_biantr(ph, ps, ch):
    s15 = R_id(f"↔{ch}{ps}")
    s16 = R_bibi2d(f"↔{ch}{ps}", f"{ch}", f"{ps}", f"{ph}", s15)
    return R_biimparc(f"↔{ch}{ps}", f"↔{ph}{ch}", f"↔{ph}{ps}", s16)

@Theorem(3, "pm4.14")
def R_pm4_14(ph, ps, ch):
    s31 = R_con34b(f"{ps}", f"{ch}")
    s32 = R_imbi2i(f"→{ps}{ch}", f"→¬{ch}¬{ps}", f"{ph}", s31)
    s36 = R_impexp(f"{ph}", f"{ps}", f"{ch}")
    s40 = R_impexp(f"{ph}", f"¬{ch}", f"¬{ps}")
    return R_3bitr4i(f"→{ph}→{ps}{ch}", f"→{ph}→¬{ch}¬{ps}", f"→∧{ph}{ps}{ch}", f"→∧{ph}¬{ch}¬{ps}", s32, s36, s40)

@Theorem(3, "pm3.37")
def R_pm3_37(ph, ps, ch):
    s15 = R_pm4_14(f"{ph}", f"{ps}", f"{ch}")
    return R_biimpi(f"→∧{ph}{ps}{ch}", f"→∧{ph}¬{ch}¬{ps}", s15)

@Theorem(4, "anim12")
def R_anim12(ph, ps, ch, th):
    s13 = R_id(f"→{ph}{ps}")
    s15 = R_id(f"→{ch}{th}")
    return R_im2anan9(f"→{ph}{ps}", f"{ph}", f"{ps}", f"→{ch}{th}", f"{ch}", f"{th}", s13, s15)

@Theorem(2, "pm3.4")
def R_pm3_4(ph, ps):
    s7 = R_simpr(f"{ph}", f"{ps}")
    return R_a1d(f"∧{ph}{ps}", f"{ps}", f"{ph}", s7)

def R_exbiri(ph, ps, ch, th, h1):
    s10 = R_biimpar(f"∧{ph}{ps}", f"{ch}", f"{th}", h1)
    return R_exp31(f"{ph}", f"{ps}", f"{th}", f"{ch}", s10)

def R_pm2_61ian(ph, ps, ch, h1, h2):
    s8 = R_ex(f"{ph}", f"{ps}", f"{ch}", h1)
    s14 = R_ex(f"¬{ph}", f"{ps}", f"{ch}", h2)
    return R_pm2_61i(f"{ph}", f"→{ps}{ch}", s8, s14)

def R_pm2_61dan(ph, ps, ch, h1, h2):
    s7 = R_ex(f"{ph}", f"{ps}", f"{ch}", h1)
    s13 = R_ex(f"{ph}", f"¬{ps}", f"{ch}", h2)
    return R_pm2_61d(f"{ph}", f"{ps}", f"{ch}", s7, s13)

def R_pm2_61ddan(ph, ps, ch, th, h1, h2, h3):
    s16 = R_adantlr(f"{ph}", f"{ch}", f"{th}", f"¬{ps}", h2)
    s23 = R_anassrs(f"{ph}", f"¬{ps}", f"¬{ch}", f"{th}", h3)
    s24 = R_pm2_61dan(f"∧{ph}¬{ps}", f"{ch}", f"{th}", s16, s23)
    return R_pm2_61dan(f"{ph}", f"{ps}", f"{th}", h1, s24)

def R_pm2_61dda(ph, ps, ch, th, h1, h2, h3):
    s13 = R_anassrs(f"{ph}", f"{ps}", f"{ch}", f"{th}", h3)
    s20 = R_adantlr(f"{ph}", f"¬{ch}", f"{th}", f"{ps}", h2)
    s21 = R_pm2_61dan(f"∧{ph}{ps}", f"{ch}", f"{th}", s13, s20)
    return R_pm2_61dan(f"{ph}", f"{ps}", f"{th}", s21, h1)

def R_mtand(ph, ps, ch, h1, h2):
    s8 = R_ex(f"{ph}", f"{ps}", f"{ch}", h2)
    return R_mtod(f"{ph}", f"{ps}", f"{ch}", h1, s8)

def R_pm2_65da(ph, ps, ch, h1, h2):
    s7 = R_ex(f"{ph}", f"{ps}", f"{ch}", h1)
    s13 = R_ex(f"{ph}", f"{ps}", f"¬{ch}", h2)
    return R_pm2_65d(f"{ph}", f"{ps}", f"{ch}", s7, s13)

def R_condan(ph, ps, ch, h1, h2):
    s8 = R_pm2_65da(f"{ph}", f"¬{ps}", f"{ch}", h1, h2)
    return R_notnotrd(f"{ph}", f"{ps}", s8)

@Theorem(3, "biadan")
def R_biadan(ph, ps, ch):
    s30 = R_pm4_71r(f"{ph}", f"{ps}")
    s33 = R_bicom(f"{ph}", f"∧{ps}{ph}")
    s54 = R_bicom(f"{ph}", f"∧{ps}{ch}")
    s58 = R_pm5_32(f"{ps}", f"{ph}", f"{ch}")
    s59 = R_bibi12i(f"↔{ph}∧{ps}{ch}", f"↔∧{ps}{ch}{ph}", f"→{ps}↔{ph}{ch}", f"↔∧{ps}{ph}∧{ps}{ch}", s54, s58)
    s62 = R_bicom(f"→{ps}↔{ph}{ch}", f"↔{ph}∧{ps}{ch}")
    s66 = R_biluk(f"∧{ps}{ph}", f"{ph}", f"∧{ps}{ch}")
    s67 = R_3bitr4ri(f"↔↔{ph}∧{ps}{ch}→{ps}↔{ph}{ch}", f"↔↔∧{ps}{ch}{ph}↔∧{ps}{ph}∧{ps}{ch}", f"↔→{ps}↔{ph}{ch}↔{ph}∧{ps}{ch}", f"↔∧{ps}{ph}{ph}", s59, s62, s66)
    return R_3bitri(f"→{ph}{ps}", f"↔{ph}∧{ps}{ph}", f"↔∧{ps}{ph}{ph}", f"↔→{ps}↔{ph}{ch}↔{ph}∧{ps}{ch}", s30, s33, s67)

def R_biadani(ph, ps, ch, h1):
    s18 = R_biadan(f"{ph}", f"{ps}", f"{ch}")
    return R_mpbi(f"→{ph}{ps}", f"↔→{ps}↔{ph}{ch}↔{ph}∧{ps}{ch}", h1, s18)

def R_biadanii(ph, ps, ch, h1, h2):
    s15 = R_biadani(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_mpbi(f"→{ps}↔{ph}{ch}", f"↔{ph}∧{ps}{ch}", h2, s15)

def R_biadanid(ph, ps, ch, th, h1, h2):
    s27 = R_biimpa(f"∧{ph}{ch}", f"{ps}", f"{th}", h2)
    s28 = R_an32s(f"{ph}", f"{ch}", f"{ps}", f"{th}", s27)
    s29 = R_mpdan(f"∧{ph}{ps}", f"{ch}", f"{th}", h1, s28)
    s30 = R_jca(f"∧{ph}{ps}", f"{ch}", f"{th}", h1, s29)
    s39 = R_biimpar(f"∧{ph}{ch}", f"{ps}", f"{th}", h2)
    s40 = R_anasss(f"{ph}", f"{ch}", f"{th}", f"{ps}", s39)
    return R_impbida(f"{ph}", f"{ps}", f"∧{ch}{th}", s30, s40)

@Theorem(2, "pm5.1")
def R_pm5_1(ph, ps):
    s7 = R_pm5_501(f"{ph}", f"{ps}")
    return R_biimpa(f"{ph}", f"{ps}", f"↔{ph}{ps}", s7)

@Theorem(2, "pm5.21")
def R_pm5_21(ph, ps):
    s9 = R_pm5_21im(f"{ph}", f"{ps}")
    return R_imp(f"¬{ph}", f"¬{ps}", f"↔{ph}{ps}", s9)

@Theorem(3, "pm5.35")
def R_pm5_35(ph, ps, ch):
    s14 = R_pm5_1(f"→{ph}{ps}", f"→{ph}{ch}")
    return R_pm5_74rd(f"∧→{ph}{ps}→{ph}{ch}", f"{ph}", f"{ps}", f"{ch}", s14)

@Theorem(2, "abai")
def R_abai(ph, ps):
    s7 = R_biimt(f"{ph}", f"{ps}")
    return R_pm5_32i(f"{ph}", f"{ps}", f"→{ph}{ps}", s7)

@Theorem(2, "pm4.45im")
def R_pm4_45im(ph, ps):
    s6 = R_ax_1(f"{ph}", f"{ps}")
    return R_pm4_71i(f"{ph}", f"→{ps}{ph}", s6)

@Theorem(2, "impimprbi")
def R_impimprbi(ph, ps):
    s21 = R_dfbi2(f"{ph}", f"{ps}")
    s24 = R_pm5_1(f"→{ph}{ps}", f"→{ps}{ph}")
    s25 = R_sylbi(f"↔{ph}{ps}", f"∧→{ph}{ps}→{ps}{ph}", f"↔→{ph}{ps}→{ps}{ph}", s21, s24)
    s31 = R_impbi(f"{ph}", f"{ps}")
    s38 = R_pm2_521(f"{ph}", f"{ps}")
    s39 = R_pm2_24d(f"¬→{ph}{ps}", f"→{ps}{ph}", f"↔{ph}{ps}", s38)
    s40 = R_bija(f"→{ph}{ps}", f"→{ps}{ph}", f"↔{ph}{ps}", s31, s39)
    return R_impbii(f"↔{ph}{ps}", f"↔→{ph}{ps}→{ps}{ph}", s25, s40)

@Theorem(3, "nan")
def R_nan(ph, ps, ch):
    s23 = R_impexp(f"{ph}", f"{ps}", f"¬{ch}")
    s29 = R_imnan(f"{ps}", f"{ch}")
    s30 = R_imbi2i(f"→{ps}¬{ch}", f"¬∧{ps}{ch}", f"{ph}", s29)
    return R_bitr2i(f"→∧{ph}{ps}¬{ch}", f"→{ph}→{ps}¬{ch}", f"→{ph}¬∧{ps}{ch}", s23, s30)

@Theorem(3, "pm5.31")
def R_pm5_31(ph, ps, ch):
    s11 = R_simpr(f"{ch}", f"→{ph}{ps}")
    s14 = R_simpl(f"{ch}", f"→{ph}{ps}")
    return R_jctird(f"∧{ch}→{ph}{ps}", f"{ph}", f"{ps}", f"{ch}", s11, s14)

@Theorem(3, "pm5.31r")
def R_pm5_31r(ph, ps, ch):
    s10 = R_ax_1(f"{ch}", f"{ph}")
    s12 = R_id(f"→{ph}{ps}")
    return R_anim12ii(f"{ch}", f"{ph}", f"{ch}", f"→{ph}{ps}", f"{ps}", s10, s12)

@Theorem(3, "pm4.15")
def R_pm4_15(ph, ps, ch):
    s19 = R_con2b(f"∧{ps}{ch}", f"{ph}")
    s23 = R_nan(f"{ph}", f"{ps}", f"{ch}")
    return R_bitr2i(f"→∧{ps}{ch}¬{ph}", f"→{ph}¬∧{ps}{ch}", f"→∧{ph}{ps}¬{ch}", s19, s23)

@Theorem(2, "pm5.36")
def R_pm5_36(ph, ps):
    s7 = R_id(f"↔{ph}{ps}")
    return R_pm5_32ri(f"↔{ph}{ps}", f"{ph}", f"{ps}", s7)

@Theorem(2, "annotanannot")
def R_annotanannot(ph, ps):
    s16 = R_ibar(f"{ph}", f"{ps}")
    s17 = R_bicomd(f"{ph}", f"{ps}", f"∧{ph}{ps}", s16)
    s18 = R_notbid(f"{ph}", f"∧{ph}{ps}", f"{ps}", s17)
    return R_pm5_32i(f"{ph}", f"¬∧{ph}{ps}", f"¬{ps}", s18)

@Theorem(3, "pm5.33")
def R_pm5_33(ph, ps, ch):
    s16 = R_ibar(f"{ph}", f"{ps}")
    s17 = R_imbi1d(f"{ph}", f"{ps}", f"∧{ph}{ps}", f"{ch}", s16)
    return R_pm5_32i(f"{ph}", f"→{ps}{ch}", f"→∧{ph}{ps}{ch}", s17)

def R_syl12anc(ph, ps, ch, th, ta, h1, h2, h3, h4):
    s12 = R_jca(f"{ph}", f"{ch}", f"{th}", h2, h3)
    return R_syl2anc(f"{ph}", f"{ps}", f"∧{ch}{th}", f"{ta}", h1, s12, h4)

def R_syl21anc(ph, ps, ch, th, ta, h1, h2, h3, h4):
    s11 = R_jca(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    return R_syl2anc(f"{ph}", f"∧{ps}{ch}", f"{th}", f"{ta}", s11, h3, h4)

def R_syl22anc(ph, ps, ch, th, ta, et, h1, h2, h3, h4, h5):
    s12 = R_jca(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    return R_syl12anc(f"{ph}", f"∧{ps}{ch}", f"{th}", f"{ta}", f"{et}", s12, h3, h4, h5)

def R_syl1111anc(ph, ps, ch, th, ta, et, h1, h2, h3, h4, h5):
    s12 = R_jca(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    return R_syl21anc(f"{ph}", f"∧{ps}{ch}", f"{th}", f"{ta}", f"{et}", s12, h3, h4, h5)

def R_syldbl2(ph, ps, ch, h1):
    s9 = R_com12(f"∧{ph}{ps}", f"{ps}", f"{ch}", h1)
    return R_anabsi7(f"{ph}", f"{ps}", f"{ch}", s9)

def R_mpsyl4anc(ph, ps, ch, th, ta, et, h1, h2, h3, h4, h5):
    s9 = R_a1i(f"{ph}", f"{th}", h1)
    s13 = R_a1i(f"{ps}", f"{th}", h2)
    s17 = R_a1i(f"{ch}", f"{th}", h3)
    return R_syl1111anc(f"{th}", f"{ph}", f"{ps}", f"{ch}", f"{ta}", f"{et}", s9, s13, s17, h4, h5)

@Theorem(3, "pm4.87")
def R_pm4_87(ph, ps, ch):
    s36 = R_impexp(f"{ph}", f"{ps}", f"{ch}")
    s40 = R_bi2_04(f"{ph}", f"{ps}", f"{ch}")
    s41 = R_pm3_2i(f"↔→∧{ph}{ps}{ch}→{ph}→{ps}{ch}", f"↔→{ph}→{ps}{ch}→{ps}→{ph}{ch}", s36, s40)
    s47 = R_impexp(f"{ps}", f"{ph}", f"{ch}")
    s48 = R_bicomi(f"→∧{ps}{ph}{ch}", f"→{ps}→{ph}{ch}", s47)
    return R_pm3_2i(f"∧↔→∧{ph}{ps}{ch}→{ph}→{ps}{ch}↔→{ph}→{ps}{ch}→{ps}→{ph}{ch}", f"↔→{ps}→{ph}{ch}→∧{ps}{ph}{ch}", s41, s48)

@Theorem(3, "bimsc1")
def R_bimsc1(ph, ps, ch):
    s15 = R_id(f"↔{ch}∧{ps}{ph}")
    s21 = R_simpr(f"{ps}", f"{ph}")
    s24 = R_ancr(f"{ph}", f"{ps}")
    s25 = R_impbid2(f"→{ph}{ps}", f"∧{ps}{ph}", f"{ph}", s21, s24)
    return R_sylan9bbr(f"↔{ch}∧{ps}{ph}", f"{ch}", f"∧{ps}{ph}", f"→{ph}{ps}", f"{ph}", s15, s25)

def R_a2and(ph, ps, ch, th, ta, et, h1, h2):
    s33 = R_expd(f"{ph}", f"{ps}", f"{et}", f"{ch}", h2)
    s34 = R_imdistand(f"{ph}", f"{ps}", f"{et}", f"{ch}", s33)
    s42 = R_imim1(f"∧{ps}{ch}", f"{ta}", f"{th}")
    s43 = R_com3l(f"→∧{ps}{ch}{ta}", f"→{ta}{th}", f"∧{ps}{ch}", f"{th}", s42)
    s44 = R_syl6c(f"{ph}", f"∧{ps}{et}", f"→{ta}{th}", f"∧{ps}{ch}", f"→→∧{ps}{ch}{ta}{th}", h1, s34, s43)
    return R_com23(f"{ph}", f"∧{ps}{et}", f"→∧{ps}{ch}{ta}", f"{th}", s44)

def R_animpimp2impd(ph, ps, ch, th, ta, et, h1, h2):
    s33 = R_expr(f"{ps}", f"{ph}", f"{th}", f"→{et}{ta}", h2)
    s34 = R_a2d(f"∧{ps}{ph}", f"{th}", f"{et}", f"{ta}", s33)
    s35 = R_syld(f"∧{ps}{ph}", f"{ch}", f"→{th}{et}", f"→{th}{ta}", h1, s34)
    s36 = R_expcom(f"{ps}", f"{ph}", f"→{ch}→{th}{ta}", s35)
    return R_a2d(f"{ph}", f"{ps}", f"{ch}", f"→{th}{ta}", s36)

@Theorem(2, "pm4.64")
def R_pm4_64(ph, ps):
    s9 = R_df_or(f"{ph}", f"{ps}")
    return R_bicomi(f"∨{ph}{ps}", f"→¬{ph}{ps}", s9)

@Theorem(2, "pm4.66")
def R_pm4_66(ph, ps):
    return R_pm4_64(f"{ph}", f"¬{ps}")

@Theorem(2, "pm2.53")
def R_pm2_53(ph, ps):
    s9 = R_df_or(f"{ph}", f"{ps}")
    return R_biimpi(f"∨{ph}{ps}", f"→¬{ph}{ps}", s9)

@Theorem(2, "pm2.54")
def R_pm2_54(ph, ps):
    s9 = R_df_or(f"{ph}", f"{ps}")
    return R_biimpri(f"∨{ph}{ps}", f"→¬{ph}{ps}", s9)

@Theorem(2, "imor")
def R_imor(ph, ps):
    s17 = R_notnotb(f"{ph}")
    s18 = R_imbi1i(f"{ph}", f"¬¬{ph}", f"{ps}", s17)
    s21 = R_df_or(f"¬{ph}", f"{ps}")
    return R_bitr4i(f"→{ph}{ps}", f"→¬¬{ph}{ps}", f"∨¬{ph}{ps}", s18, s21)

def R_imori(ph, ps, h1):
    s10 = R_imor(f"{ph}", f"{ps}")
    return R_mpbi(f"→{ph}{ps}", f"∨¬{ph}{ps}", h1, s10)

def R_imorri(ph, ps, h1):
    s10 = R_imor(f"{ph}", f"{ps}")
    return R_mpbir(f"→{ph}{ps}", f"∨¬{ph}{ps}", h1, s10)

@Theorem(2, "pm4.62")
def R_pm4_62(ph, ps):
    return R_imor(f"{ph}", f"¬{ps}")

def R_jaoi(ph, ps, ch, h1, h2):
    s13 = R_pm2_53(f"{ph}", f"{ch}")
    s15 = R_syl6(f"∨{ph}{ch}", f"¬{ph}", f"{ch}", f"{ps}", s13, h2)
    return R_pm2_61d2(f"∨{ph}{ch}", f"{ph}", f"{ps}", s15, h1)

def R_jao1i(ph, ps, ch, h1):
    s7 = R_ax_1(f"{ph}", f"{ch}")
    return R_jaoi(f"{ph}", f"→{ch}{ph}", f"{ps}", s7, h1)

def R_jaod(ph, ps, ch, th, h1, h2):
    s14 = R_com12(f"{ph}", f"{ps}", f"{ch}", h1)
    s19 = R_com12(f"{ph}", f"{th}", f"{ch}", h2)
    s20 = R_jaoi(f"{ps}", f"→{ph}{ch}", f"{th}", s14, s19)
    return R_com12(f"∨{ps}{th}", f"{ph}", f"{ch}", s20)

def R_mpjaod(ph, ps, ch, th, h1, h2, h3):
    s12 = R_jaod(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2)
    return R_mpd(f"{ph}", f"∨{ps}{th}", f"{ch}", h3, s12)

def R_ori(ph, ps, h1):
    s10 = R_df_or(f"{ph}", f"{ps}")
    return R_mpbi(f"∨{ph}{ps}", f"→¬{ph}{ps}", h1, s10)

def R_orri(ph, ps, h1):
    s10 = R_df_or(f"{ph}", f"{ps}")
    return R_mpbir(f"∨{ph}{ps}", f"→¬{ph}{ps}", h1, s10)

def R_orrd(ph, ps, ch, h1):
    s11 = R_pm2_54(f"{ps}", f"{ch}")
    return R_syl(f"{ph}", f"→¬{ps}{ch}", f"∨{ps}{ch}", h1, s11)

def R_ord(ph, ps, ch, h1):
    s11 = R_df_or(f"{ps}", f"{ch}")
    return R_sylib(f"{ph}", f"∨{ps}{ch}", f"→¬{ps}{ch}", h1, s11)

def R_orci(ph, ps, h1):
    s5 = R_pm2_24i(f"{ph}", f"{ps}", h1)
    return R_orri(f"{ph}", f"{ps}", s5)

def R_olci(ph, ps, h1):
    s6 = R_a1i(f"{ph}", f"¬{ps}", h1)
    return R_orri(f"{ps}", f"{ph}", s6)

@Theorem(2, "orc")
def R_orc(ph, ps):
    s5 = R_pm2_24(f"{ph}", f"{ps}")
    return R_orrd(f"{ph}", f"{ph}", f"{ps}", s5)

@Theorem(2, "olc")
def R_olc(ph, ps):
    s6 = R_ax_1(f"{ph}", f"¬{ps}")
    return R_orrd(f"{ph}", f"{ps}", f"{ph}", s6)

@Theorem(2, "pm1.4")
def R_pm1_4(ph, ps):
    s7 = R_olc(f"{ph}", f"{ps}")
    s10 = R_orc(f"{ps}", f"{ph}")
    return R_jaoi(f"{ph}", f"∨{ps}{ph}", f"{ps}", s7, s10)

@Theorem(2, "orcom")
def R_orcom(ph, ps):
    s8 = R_pm1_4(f"{ph}", f"{ps}")
    s11 = R_pm1_4(f"{ps}", f"{ph}")
    return R_impbii(f"∨{ph}{ps}", f"∨{ps}{ph}", s8, s11)

def R_orcomd(ph, ps, ch, h1):
    s10 = R_orcom(f"{ps}", f"{ch}")
    return R_sylib(f"{ph}", f"∨{ps}{ch}", f"∨{ch}{ps}", h1, s10)

def R_orcoms(ph, ps, ch, h1):
    s9 = R_pm1_4(f"{ps}", f"{ph}")
    return R_syl(f"∨{ps}{ph}", f"∨{ph}{ps}", f"{ch}", s9, h1)

def R_orcd(ph, ps, ch, h1):
    s8 = R_orc(f"{ps}", f"{ch}")
    return R_syl(f"{ph}", f"{ps}", f"∨{ps}{ch}", h1, s8)

def R_olcd(ph, ps, ch, h1):
    s7 = R_orcd(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_orcomd(f"{ph}", f"{ps}", f"{ch}", s7)

def R_orcs(ph, ps, ch, h1):
    s7 = R_orc(f"{ph}", f"{ps}")
    return R_syl(f"{ph}", f"∨{ph}{ps}", f"{ch}", s7, h1)

def R_olcs(ph, ps, ch, h1):
    s7 = R_orcoms(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_orcs(f"{ps}", f"{ph}", f"{ch}", s7)

def R_olcnd(ph, ps, ch, h1, h2):
    s8 = R_ord(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_mt3d(f"{ph}", f"{ps}", f"{ch}", h2, s8)

def R_orcnd(ph, ps, ch, h1, h2):
    s7 = R_orcomd(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_olcnd(f"{ph}", f"{ch}", f"{ps}", s7, h2)

def R_mtord(ph, ps, ch, th, h1, h2, h3):
    s16 = R_pm2_53(f"{ch}", f"{th}")
    s17 = R_syl6ci(f"{ph}", f"{ps}", f"∨{ch}{th}", f"¬{ch}", f"{th}", h3, h1, s16)
    return R_mtod(f"{ph}", f"{ps}", f"{th}", h2, s17)

def R_pm3_2ni(ph, ps, h1, h2):
    s9 = R_id(f"{ph}")
    s13 = R_pm2_21i(f"{ps}", f"{ph}", h2)
    s14 = R_jaoi(f"{ph}", f"{ph}", f"{ps}", s9, s13)
    return R_mto(f"∨{ph}{ps}", f"{ph}", h1, s14)

@Theorem(2, "pm2.45")
def R_pm2_45(ph, ps):
    s6 = R_orc(f"{ph}", f"{ps}")
    return R_con3i(f"{ph}", f"∨{ph}{ps}", s6)

@Theorem(2, "pm2.46")
def R_pm2_46(ph, ps):
    s6 = R_olc(f"{ps}", f"{ph}")
    return R_con3i(f"{ps}", f"∨{ph}{ps}", s6)

@Theorem(2, "pm2.47")
def R_pm2_47(ph, ps):
    s9 = R_pm2_45(f"{ph}", f"{ps}")
    return R_orcd(f"¬∨{ph}{ps}", f"¬{ph}", f"{ps}", s9)

@Theorem(2, "pm2.48")
def R_pm2_48(ph, ps):
    s9 = R_pm2_46(f"{ph}", f"{ps}")
    return R_olcd(f"¬∨{ph}{ps}", f"¬{ps}", f"{ph}", s9)

@Theorem(2, "pm2.49")
def R_pm2_49(ph, ps):
    s10 = R_pm2_46(f"{ph}", f"{ps}")
    return R_olcd(f"¬∨{ph}{ps}", f"¬{ps}", f"¬{ph}", s10)

@Theorem(2, "norbi")
def R_norbi(ph, ps):
    s7 = R_orc(f"{ph}", f"{ps}")
    s10 = R_olc(f"{ps}", f"{ph}")
    return R_pm5_21ni(f"{ph}", f"∨{ph}{ps}", f"{ps}", s7, s10)

@Theorem(2, "nbior")
def R_nbior(ph, ps):
    s8 = R_norbi(f"{ph}", f"{ps}")
    return R_con1i(f"∨{ph}{ps}", f"↔{ph}{ps}", s8)

@Theorem(2, "orel1")
def R_orel1(ph, ps):
    s8 = R_pm2_53(f"{ph}", f"{ps}")
    return R_com12(f"∨{ph}{ps}", f"¬{ph}", f"{ps}", s8)

@Theorem(2, "pm2.25")
def R_pm2_25(ph, ps):
    s8 = R_orel1(f"{ph}", f"{ps}")
    return R_orri(f"{ph}", f"→∨{ph}{ps}{ps}", s8)

@Theorem(2, "orel2")
def R_orel2(ph, ps):
    s8 = R_idd(f"¬{ph}", f"{ps}")
    s11 = R_pm2_21(f"{ph}", f"{ps}")
    return R_jaod(f"¬{ph}", f"{ps}", f"{ps}", f"{ph}", s8, s11)

@Theorem(3, "pm2.67-2")
def R_pm2_67_2(ph, ps, ch):
    s7 = R_orc(f"{ph}", f"{ch}")
    return R_imim1i(f"{ph}", f"∨{ph}{ch}", f"{ps}", s7)

@Theorem(2, "pm2.67")
def R_pm2_67(ph, ps):
    return R_pm2_67_2(f"{ph}", f"{ps}", f"{ps}")

@Theorem(2, "curryax")
def R_curryax(ph, ps):
    s6 = R_pm2_21(f"{ph}", f"{ps}")
    return R_orri(f"{ph}", f"→{ph}{ps}", s6)

@Theorem(1, "exmid")
def R_exmid(ph):
    s5 = R_id(f"¬{ph}")
    return R_orri(f"{ph}", f"¬{ph}", s5)

@Theorem(2, "exmidd")
def R_exmidd(ph, ps):
    s6 = R_exmid(f"{ps}")
    return R_a1i(f"∨{ps}¬{ps}", f"{ph}", s6)

@Theorem(1, "pm2.1")
def R_pm2_1(ph):
    s3 = R_id(f"{ph}")
    return R_imori(f"{ph}", f"{ph}", s3)

@Theorem(1, "pm2.13")
def R_pm2_13(ph):
    s7 = R_notnot(f"¬{ph}")
    return R_orri(f"{ph}", f"¬¬¬{ph}", s7)

@Theorem(2, "pm2.621")
def R_pm2_621(ph, ps):
    s8 = R_id(f"→{ph}{ps}")
    s11 = R_idd(f"→{ph}{ps}", f"{ps}")
    return R_jaod(f"→{ph}{ps}", f"{ph}", f"{ps}", f"{ps}", s8, s11)

@Theorem(2, "pm2.62")
def R_pm2_62(ph, ps):
    s9 = R_pm2_621(f"{ph}", f"{ps}")
    return R_com12(f"→{ph}{ps}", f"∨{ph}{ps}", f"{ps}", s9)

@Theorem(2, "pm2.68")
def R_pm2_68(ph, ps):
    s10 = R_jarl(f"{ph}", f"{ps}", f"{ps}")
    return R_orrd(f"→→{ph}{ps}{ps}", f"{ph}", f"{ps}", s10)

@Theorem(2, "dfor2")
def R_dfor2(ph, ps):
    s10 = R_pm2_62(f"{ph}", f"{ps}")
    s13 = R_pm2_68(f"{ph}", f"{ps}")
    return R_impbii(f"∨{ph}{ps}", f"→→{ph}{ps}{ps}", s10, s13)

@Theorem(1, "pm2.07")
def R_pm2_07(ph):
    return R_olc(f"{ph}", f"{ph}")

@Theorem(1, "pm1.2")
def R_pm1_2(ph):
    s4 = R_id(f"{ph}")
    return R_jaoi(f"{ph}", f"{ph}", f"{ph}", s4, s4)

@Theorem(1, "oridm")
def R_oridm(ph):
    s5 = R_pm1_2(f"{ph}")
    s7 = R_pm2_07(f"{ph}")
    return R_impbii(f"∨{ph}{ph}", f"{ph}", s5, s7)

@Theorem(1, "pm4.25")
def R_pm4_25(ph):
    s5 = R_oridm(f"{ph}")
    return R_bicomi(f"∨{ph}{ph}", f"{ph}", s5)

@Theorem(2, "pm2.4")
def R_pm2_4(ph, ps):
    s8 = R_orc(f"{ph}", f"{ps}")
    s10 = R_id(f"∨{ph}{ps}")
    return R_jaoi(f"{ph}", f"∨{ph}{ps}", f"∨{ph}{ps}", s8, s10)

@Theorem(2, "pm2.41")
def R_pm2_41(ph, ps):
    s8 = R_olc(f"{ps}", f"{ph}")
    s10 = R_id(f"∨{ph}{ps}")
    return R_jaoi(f"{ps}", f"∨{ph}{ps}", f"∨{ph}{ps}", s8, s10)

def R_orim12i(ph, ps, ch, th, h1, h2):
    s9 = R_orcd(f"{ph}", f"{ps}", f"{th}", h1)
    s14 = R_olcd(f"{ch}", f"{th}", f"{ps}", h2)
    return R_jaoi(f"{ph}", f"∨{ps}{th}", f"{ch}", s9, s14)

def R_orim1i(ph, ps, ch, h1):
    s6 = R_id(f"{ch}")
    return R_orim12i(f"{ph}", f"{ps}", f"{ch}", f"{ch}", h1, s6)

def R_orim2i(ph, ps, ch, h1):
    s5 = R_id(f"{ch}")
    return R_orim12i(f"{ch}", f"{ch}", f"{ph}", f"{ps}", s5, h1)

def R_orbi2i(ph, ps, ch, h1):
    s12 = R_biimpi(f"{ph}", f"{ps}", h1)
    s13 = R_orim2i(f"{ph}", f"{ps}", f"{ch}", s12)
    s20 = R_biimpri(f"{ph}", f"{ps}", h1)
    s21 = R_orim2i(f"{ps}", f"{ph}", f"{ch}", s20)
    return R_impbii(f"∨{ch}{ph}", f"∨{ch}{ps}", s13, s21)

def R_orbi1i(ph, ps, ch, h1):
    s14 = R_orcom(f"{ph}", f"{ch}")
    s19 = R_orbi2i(f"{ph}", f"{ps}", f"{ch}", h1)
    s22 = R_orcom(f"{ch}", f"{ps}")
    return R_3bitri(f"∨{ph}{ch}", f"∨{ch}{ph}", f"∨{ch}{ps}", f"∨{ps}{ch}", s14, s19, s22)

def R_orbi12i(ph, ps, ch, th, h1, h2):
    s13 = R_orbi2i(f"{ch}", f"{th}", f"{ph}", h2)
    s18 = R_orbi1i(f"{ph}", f"{ps}", f"{th}", h1)
    return R_bitri(f"∨{ph}{ch}", f"∨{ph}{th}", f"∨{ps}{th}", s13, s18)

def R_orbi2d(ph, ps, ch, th, h1):
    s20 = R_imbi2d(f"{ph}", f"{ps}", f"{ch}", f"¬{th}", h1)
    s23 = R_df_or(f"{th}", f"{ps}")
    s26 = R_df_or(f"{th}", f"{ch}")
    return R_3bitr4g(f"{ph}", f"→¬{th}{ps}", f"→¬{th}{ch}", f"∨{th}{ps}", f"∨{th}{ch}", s20, s23, s26)

def R_orbi1d(ph, ps, ch, th, h1):
    s18 = R_orbi2d(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    s21 = R_orcom(f"{ps}", f"{th}")
    s24 = R_orcom(f"{ch}", f"{th}")
    return R_3bitr4g(f"{ph}", f"∨{th}{ps}", f"∨{th}{ch}", f"∨{ps}{th}", f"∨{ch}{th}", s18, s21, s24)

@Theorem(3, "orbi1")
def R_orbi1(ph, ps, ch):
    s8 = R_id(f"↔{ph}{ps}")
    return R_orbi1d(f"↔{ph}{ps}", f"{ph}", f"{ps}", f"{ch}", s8)

def R_orbi12d(ph, ps, ch, th, ta, h1, h2):
    s15 = R_orbi1d(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1)
    s21 = R_orbi2d(f"{ph}", f"{th}", f"{ta}", f"{ch}", h2)
    return R_bitrd(f"{ph}", f"∨{ps}{th}", f"∨{ch}{th}", f"∨{ch}{ta}", s15, s21)

@Theorem(3, "pm1.5")
def R_pm1_5(ph, ps, ch):
    s15 = R_orc(f"{ph}", f"{ch}")
    s16 = R_olcd(f"{ph}", f"∨{ph}{ch}", f"{ps}", s15)
    s22 = R_olc(f"{ch}", f"{ph}")
    s23 = R_orim2i(f"{ch}", f"∨{ph}{ch}", f"{ps}", s22)
    return R_jaoi(f"{ph}", f"∨{ps}∨{ph}{ch}", f"∨{ps}{ch}", s16, s23)

@Theorem(3, "or12")
def R_or12(ph, ps, ch):
    s13 = R_pm1_5(f"{ph}", f"{ps}", f"{ch}")
    s17 = R_pm1_5(f"{ps}", f"{ph}", f"{ch}")
    return R_impbii(f"∨{ph}∨{ps}{ch}", f"∨{ps}∨{ph}{ch}", s13, s17)

@Theorem(3, "orass")
def R_orass(ph, ps, ch):
    s23 = R_orcom(f"∨{ph}{ps}", f"{ch}")
    s27 = R_or12(f"{ch}", f"{ph}", f"{ps}")
    s33 = R_orcom(f"{ch}", f"{ps}")
    s34 = R_orbi2i(f"∨{ch}{ps}", f"∨{ps}{ch}", f"{ph}", s33)
    return R_3bitri(f"∨∨{ph}{ps}{ch}", f"∨{ch}∨{ph}{ps}", f"∨{ph}∨{ch}{ps}", f"∨{ph}∨{ps}{ch}", s23, s27, s34)

@Theorem(3, "pm2.31")
def R_pm2_31(ph, ps, ch):
    s13 = R_orass(f"{ph}", f"{ps}", f"{ch}")
    return R_biimpri(f"∨∨{ph}{ps}{ch}", f"∨{ph}∨{ps}{ch}", s13)

@Theorem(3, "pm2.32")
def R_pm2_32(ph, ps, ch):
    s13 = R_orass(f"{ph}", f"{ps}", f"{ch}")
    return R_biimpi(f"∨∨{ph}{ps}{ch}", f"∨{ph}∨{ps}{ch}", s13)

@Theorem(3, "pm2.3")
def R_pm2_3(ph, ps, ch):
    s9 = R_pm1_4(f"{ps}", f"{ch}")
    return R_orim2i(f"∨{ps}{ch}", f"∨{ch}{ps}", f"{ph}", s9)

@Theorem(3, "or32")
def R_or32(ph, ps, ch):
    s22 = R_orass(f"{ph}", f"{ps}", f"{ch}")
    s26 = R_or12(f"{ph}", f"{ps}", f"{ch}")
    s29 = R_orcom(f"{ps}", f"∨{ph}{ch}")
    return R_3bitri(f"∨∨{ph}{ps}{ch}", f"∨{ph}∨{ps}{ch}", f"∨{ps}∨{ph}{ch}", f"∨∨{ph}{ch}{ps}", s22, s26, s29)

@Theorem(4, "or4")
def R_or4(ph, ps, ch, th):
    s34 = R_or12(f"{ps}", f"{ch}", f"{th}")
    s35 = R_orbi2i(f"∨{ps}∨{ch}{th}", f"∨{ch}∨{ps}{th}", f"{ph}", s34)
    s39 = R_orass(f"{ph}", f"{ps}", f"∨{ch}{th}")
    s43 = R_orass(f"{ph}", f"{ch}", f"∨{ps}{th}")
    return R_3bitr4i(f"∨{ph}∨{ps}∨{ch}{th}", f"∨{ph}∨{ch}∨{ps}{th}", f"∨∨{ph}{ps}∨{ch}{th}", f"∨∨{ph}{ch}∨{ps}{th}", s35, s39, s43)

@Theorem(4, "or42")
def R_or42(ph, ps, ch, th):
    s26 = R_or4(f"{ph}", f"{ps}", f"{ch}", f"{th}")
    s32 = R_orcom(f"{ps}", f"{th}")
    s33 = R_orbi2i(f"∨{ps}{th}", f"∨{th}{ps}", f"∨{ph}{ch}", s32)
    return R_bitri(f"∨∨{ph}{ps}∨{ch}{th}", f"∨∨{ph}{ch}∨{ps}{th}", f"∨∨{ph}{ch}∨{th}{ps}", s26, s33)

@Theorem(3, "orordi")
def R_orordi(ph, ps, ch):
    s23 = R_oridm(f"{ph}")
    s24 = R_orbi1i(f"∨{ph}{ph}", f"{ph}", f"∨{ps}{ch}", s23)
    s29 = R_or4(f"{ph}", f"{ph}", f"{ps}", f"{ch}")
    return R_bitr3i(f"∨{ph}∨{ps}{ch}", f"∨∨{ph}{ph}∨{ps}{ch}", f"∨∨{ph}{ps}∨{ph}{ch}", s24, s29)

@Theorem(3, "orordir")
def R_orordir(ph, ps, ch):
    s23 = R_oridm(f"{ch}")
    s24 = R_orbi2i(f"∨{ch}{ch}", f"{ch}", f"∨{ph}{ps}", s23)
    s29 = R_or4(f"{ph}", f"{ps}", f"{ch}", f"{ch}")
    return R_bitr3i(f"∨∨{ph}{ps}{ch}", f"∨∨{ph}{ps}∨{ch}{ch}", f"∨∨{ph}{ch}∨{ps}{ch}", s24, s29)

@Theorem(3, "orimdi")
def R_orimdi(ph, ps, ch):
    s32 = R_imdi(f"¬{ph}", f"{ps}", f"{ch}")
    s35 = R_df_or(f"{ph}", f"→{ps}{ch}")
    s42 = R_df_or(f"{ph}", f"{ps}")
    s45 = R_df_or(f"{ph}", f"{ch}")
    s46 = R_imbi12i(f"∨{ph}{ps}", f"→¬{ph}{ps}", f"∨{ph}{ch}", f"→¬{ph}{ch}", s42, s45)
    return R_3bitr4i(f"→¬{ph}→{ps}{ch}", f"→→¬{ph}{ps}→¬{ph}{ch}", f"∨{ph}→{ps}{ch}", f"→∨{ph}{ps}∨{ph}{ch}", s32, s35, s46)

@Theorem(3, "pm2.76")
def R_pm2_76(ph, ps, ch):
    s15 = R_orimdi(f"{ph}", f"{ps}", f"{ch}")
    return R_biimpi(f"∨{ph}→{ps}{ch}", f"→∨{ph}{ps}∨{ph}{ch}", s15)

@Theorem(3, "pm2.85")
def R_pm2_85(ph, ps, ch):
    s15 = R_orimdi(f"{ph}", f"{ps}", f"{ch}")
    return R_biimpri(f"∨{ph}→{ps}{ch}", f"→∨{ph}{ps}∨{ph}{ch}", s15)

@Theorem(3, "pm2.75")
def R_pm2_75(ph, ps, ch):
    s14 = R_pm2_76(f"{ph}", f"{ps}", f"{ch}")
    return R_com12(f"∨{ph}→{ps}{ch}", f"∨{ph}{ps}", f"∨{ph}{ch}", s14)

@Theorem(3, "pm4.78")
def R_pm4_78(ph, ps, ch):
    s32 = R_orordi(f"¬{ph}", f"{ps}", f"{ch}")
    s35 = R_imor(f"{ph}", f"∨{ps}{ch}")
    s42 = R_imor(f"{ph}", f"{ps}")
    s45 = R_imor(f"{ph}", f"{ch}")
    s46 = R_orbi12i(f"→{ph}{ps}", f"∨¬{ph}{ps}", f"→{ph}{ch}", f"∨¬{ph}{ch}", s42, s45)
    return R_3bitr4ri(f"∨¬{ph}∨{ps}{ch}", f"∨∨¬{ph}{ps}∨¬{ph}{ch}", f"→{ph}∨{ps}{ch}", f"∨→{ph}{ps}→{ph}{ch}", s32, s35, s46)

@Theorem(2, "biort")
def R_biort(ph, ps):
    s6 = R_id(f"{ph}")
    s9 = R_orc(f"{ph}", f"{ps}")
    return R_2thd(f"{ph}", f"{ph}", f"∨{ph}{ps}", s6, s9)

@Theorem(2, "biorf")
def R_biorf(ph, ps):
    s8 = R_olc(f"{ps}", f"{ph}")
    s11 = R_orel1(f"{ph}", f"{ps}")
    return R_impbid2(f"¬{ph}", f"{ps}", f"∨{ph}{ps}", s8, s11)

@Theorem(2, "biortn")
def R_biortn(ph, ps):
    s11 = R_notnot(f"{ph}")
    s14 = R_biorf(f"¬{ph}", f"{ps}")
    return R_syl(f"{ph}", f"¬¬{ph}", f"↔{ps}∨¬{ph}{ps}", s11, s14)

def R_biorfi(ph, ps, h1):
    s10 = R_biorf(f"{ph}", f"{ps}")
    return R_ax_mp(f"¬{ph}", f"↔{ps}∨{ph}{ps}", h1, s10)

def R_biorfri(ph, ps, h1):
    s10 = R_biorfi(f"{ph}", f"{ps}", h1)
    s13 = R_orcom(f"{ph}", f"{ps}")
    return R_bitri(f"{ps}", f"∨{ph}{ps}", f"∨{ps}{ph}", s10, s13)

def R_biorfriOLD(ph, ps, h1):
    s7 = R_orc(f"{ps}", f"{ph}")
    s14 = R_pm2_53(f"{ps}", f"{ph}")
    s15 = R_mt3i(f"∨{ps}{ph}", f"{ps}", f"{ph}", h1, s14)
    return R_impbii(f"{ps}", f"∨{ps}{ph}", s7, s15)

@Theorem(2, "pm2.26")
def R_pm2_26(ph, ps):
    s8 = R_pm2_27(f"{ph}", f"{ps}")
    return R_imori(f"{ph}", f"→→{ph}{ps}{ps}", s8)

@Theorem(2, "pm2.63")
def R_pm2_63(ph, ps):
    s10 = R_pm2_53(f"{ph}", f"{ps}")
    s13 = R_idd(f"∨{ph}{ps}", f"{ps}")
    return R_jaod(f"∨{ph}{ps}", f"¬{ph}", f"{ps}", f"{ps}", s10, s13)

@Theorem(2, "pm2.64")
def R_pm2_64(ph, ps):
    s15 = R_orel2(f"{ps}", f"{ph}")
    s16 = R_jao1i(f"{ph}", f"¬{ps}", f"∨{ph}{ps}", s15)
    return R_com12(f"∨{ph}¬{ps}", f"∨{ph}{ps}", f"{ph}", s16)

@Theorem(2, "pm2.42")
def R_pm2_42(ph, ps):
    s9 = R_pm2_21(f"{ph}", f"{ps}")
    s11 = R_id(f"→{ph}{ps}")
    return R_jaoi(f"¬{ph}", f"→{ph}{ps}", f"→{ph}{ps}", s9, s11)

@Theorem(3, "pm5.11g")
def R_pm5_11g(ph, ps, ch):
    s10 = R_pm2_5g(f"{ph}", f"{ps}", f"{ch}")
    return R_orri(f"→{ph}{ps}", f"→¬{ph}{ch}", s10)

@Theorem(2, "pm5.11")
def R_pm5_11(ph, ps):
    return R_pm5_11g(f"{ph}", f"{ps}", f"{ps}")

@Theorem(2, "pm5.12")
def R_pm5_12(ph, ps):
    s9 = R_pm2_51(f"{ph}", f"{ps}")
    return R_orri(f"→{ph}{ps}", f"→{ph}¬{ps}", s9)

@Theorem(3, "pm5.14")
def R_pm5_14(ph, ps, ch):
    s9 = R_pm2_521g(f"{ph}", f"{ps}", f"{ch}")
    return R_orri(f"→{ph}{ps}", f"→{ps}{ch}", s9)

@Theorem(2, "pm5.13")
def R_pm5_13(ph, ps):
    return R_pm5_14(f"{ph}", f"{ps}", f"{ph}")

@Theorem(2, "pm5.55")
def R_pm5_55(ph, ps):
    s19 = R_biort(f"{ph}", f"{ps}")
    s20 = R_bicomd(f"{ph}", f"{ph}", f"∨{ph}{ps}", s19)
    s27 = R_biorf(f"{ph}", f"{ps}")
    s28 = R_bicomd(f"¬{ph}", f"{ps}", f"∨{ph}{ps}", s27)
    s29 = R_nsyl5(f"{ph}", f"↔∨{ph}{ps}{ph}", f"↔∨{ph}{ps}{ps}", s20, s28)
    return R_orri(f"↔∨{ph}{ps}{ph}", f"↔∨{ph}{ps}{ps}", s29)

@Theorem(2, "pm4.72")
def R_pm4_72(ph, ps):
    s16 = R_olc(f"{ps}", f"{ph}")
    s19 = R_pm2_621(f"{ph}", f"{ps}")
    s20 = R_impbid2(f"→{ph}{ps}", f"{ps}", f"∨{ph}{ps}", s16, s19)
    s27 = R_orc(f"{ph}", f"{ps}")
    s30 = R_biimpr(f"{ps}", f"∨{ph}{ps}")
    s31 = R_syl5(f"{ph}", f"∨{ph}{ps}", f"↔{ps}∨{ph}{ps}", f"{ps}", s27, s30)
    return R_impbii(f"→{ph}{ps}", f"↔{ps}∨{ph}{ps}", s20, s31)

@Theorem(3, "imimorb")
def R_imimorb(ph, ps, ch):
    s23 = R_bi2_04(f"→{ps}{ch}", f"{ph}", f"{ch}")
    s29 = R_dfor2(f"{ps}", f"{ch}")
    s30 = R_imbi2i(f"∨{ps}{ch}", f"→→{ps}{ch}{ch}", f"{ph}", s29)
    return R_bitr4i(f"→→{ps}{ch}→{ph}{ch}", f"→{ph}→→{ps}{ch}{ch}", f"→{ph}∨{ps}{ch}", s23, s30)

@Theorem(2, "oibabs")
def R_oibabs(ph, ps):
    s15 = R_norbi(f"{ph}", f"{ps}")
    s17 = R_id(f"↔{ph}{ps}")
    s18 = R_ja(f"∨{ph}{ps}", f"↔{ph}{ps}", f"↔{ph}{ps}", s15, s17)
    s21 = R_ax_1(f"↔{ph}{ps}", f"∨{ph}{ps}")
    return R_impbii(f"→∨{ph}{ps}↔{ph}{ps}", f"↔{ph}{ps}", s18, s21)

@Theorem(3, "orbidi")
def R_orbidi(ph, ps, ch):
    s32 = R_pm5_74(f"¬{ph}", f"{ps}", f"{ch}")
    s35 = R_df_or(f"{ph}", f"↔{ps}{ch}")
    s42 = R_df_or(f"{ph}", f"{ps}")
    s45 = R_df_or(f"{ph}", f"{ch}")
    s46 = R_bibi12i(f"∨{ph}{ps}", f"→¬{ph}{ps}", f"∨{ph}{ch}", f"→¬{ph}{ch}", s42, s45)
    return R_3bitr4i(f"→¬{ph}↔{ps}{ch}", f"↔→¬{ph}{ps}→¬{ph}{ch}", f"∨{ph}↔{ps}{ch}", f"↔∨{ph}{ps}∨{ph}{ch}", s32, s35, s46)

@Theorem(3, "pm5.7")
def R_pm5_7(ph, ps, ch):
    s26 = R_orbidi(f"{ch}", f"{ph}", f"{ps}")
    s33 = R_orcom(f"{ch}", f"{ph}")
    s36 = R_orcom(f"{ch}", f"{ps}")
    s37 = R_bibi12i(f"∨{ch}{ph}", f"∨{ph}{ch}", f"∨{ch}{ps}", f"∨{ps}{ch}", s33, s36)
    return R_bitr2i(f"∨{ch}↔{ph}{ps}", f"↔∨{ch}{ph}∨{ch}{ps}", f"↔∨{ph}{ch}∨{ps}{ch}", s26, s37)

def R_jaao(ph, ps, ch, th, ta, h1, h2):
    s12 = R_adantr(f"{ph}", f"→{ps}{ch}", f"{th}", h1)
    s19 = R_adantl(f"{th}", f"→{ta}{ch}", f"{ph}", h2)
    return R_jaod(f"∧{ph}{th}", f"{ps}", f"{ch}", f"{ta}", s12, s19)

def R_jaoa(ph, ps, ch, th, ta, h1, h2):
    s12 = R_adantrd(f"{ph}", f"{ps}", f"{ch}", f"{ta}", h1)
    s18 = R_adantld(f"{th}", f"{ta}", f"{ch}", f"{ps}", h2)
    return R_jaoi(f"{ph}", f"→∧{ps}{ta}{ch}", f"{th}", s12, s18)

def R_jaoian(ph, ps, ch, th, h1, h2):
    s14 = R_ex(f"{ph}", f"{ps}", f"{ch}", h1)
    s19 = R_ex(f"{th}", f"{ps}", f"{ch}", h2)
    s20 = R_jaoi(f"{ph}", f"→{ps}{ch}", f"{th}", s14, s19)
    return R_imp(f"∨{ph}{th}", f"{ps}", f"{ch}", s20)

def R_jaodan(ph, ps, ch, th, h1, h2):
    s13 = R_ex(f"{ph}", f"{ps}", f"{ch}", h1)
    s18 = R_ex(f"{ph}", f"{th}", f"{ch}", h2)
    s19 = R_jaod(f"{ph}", f"{ps}", f"{ch}", f"{th}", s13, s18)
    return R_imp(f"{ph}", f"∨{ps}{th}", f"{ch}", s19)

def R_mpjaodan(ph, ps, ch, th, h1, h2, h3):
    s12 = R_jaodan(f"{ph}", f"{ps}", f"{ch}", f"{th}", h1, h2)
    return R_mpdan(f"{ph}", f"∨{ps}{th}", f"{ch}", h3, s12)

@Theorem(3, "pm3.44")
def R_pm3_44(ph, ps, ch):
    s12 = R_id(f"→{ps}{ph}")
    s14 = R_id(f"→{ch}{ph}")
    return R_jaao(f"→{ps}{ph}", f"{ps}", f"{ph}", f"→{ch}{ph}", f"{ch}", s12, s14)

@Theorem(3, "jao")
def R_jao(ph, ps, ch):
    s14 = R_pm3_44(f"{ps}", f"{ph}", f"{ch}")
    return R_ex(f"→{ph}{ps}", f"→{ch}{ps}", f"→∨{ph}{ch}{ps}", s14)

@Theorem(3, "jaob")
def R_jaob(ph, ps, ch):
    s22 = R_pm2_67_2(f"{ph}", f"{ps}", f"{ch}")
    s28 = R_olc(f"{ch}", f"{ph}")
    s29 = R_imim1i(f"{ch}", f"∨{ph}{ch}", f"{ps}", s28)
    s30 = R_jca(f"→∨{ph}{ch}{ps}", f"→{ph}{ps}", f"→{ch}{ps}", s22, s29)
    s34 = R_pm3_44(f"{ps}", f"{ph}", f"{ch}")
    return R_impbii(f"→∨{ph}{ch}{ps}", f"∧→{ph}{ps}→{ch}{ps}", s30, s34)

@Theorem(3, "pm4.77")
def R_pm4_77(ph, ps, ch):
    s15 = R_jaob(f"{ps}", f"{ph}", f"{ch}")
    return R_bicomi(f"→∨{ps}{ch}{ph}", f"∧→{ps}{ph}→{ch}{ph}", s15)

@Theorem(4, "pm3.48")
def R_pm3_48(ph, ps, ch, th):
    s17 = R_orc(f"{ps}", f"{th}")
    s18 = R_imim2i(f"{ps}", f"∨{ps}{th}", f"{ph}", s17)
    s24 = R_olc(f"{th}", f"{ps}")
    s25 = R_imim2i(f"{th}", f"∨{ps}{th}", f"{ch}", s24)
    return R_jaao(f"→{ph}{ps}", f"{ph}", f"∨{ps}{th}", f"→{ch}{th}", f"{ch}", s18, s25)

def R_orim12d(ph, ps, ch, th, ta, h1, h2):
    s20 = R_pm3_48(f"{ps}", f"{ch}", f"{th}", f"{ta}")
    return R_syl2anc(f"{ph}", f"→{ps}{ch}", f"→{th}{ta}", f"→∨{ps}{th}∨{ch}{ta}", h1, h2, s20)

def R_orim1d(ph, ps, ch, th, h1):
    s8 = R_idd(f"{ph}", f"{th}")
    return R_orim12d(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{th}", h1, s8)

def R_orim2d(ph, ps, ch, th, h1):
    s7 = R_idd(f"{ph}", f"{th}")
    return R_orim12d(f"{ph}", f"{th}", f"{th}", f"{ps}", f"{ch}", s7, h1)

@Theorem(3, "orim2")
def R_orim2(ph, ps, ch):
    s8 = R_id(f"→{ps}{ch}")
    return R_orim2d(f"→{ps}{ch}", f"{ps}", f"{ch}", f"{ph}", s8)

@Theorem(3, "pm2.38")
def R_pm2_38(ph, ps, ch):
    s8 = R_id(f"→{ps}{ch}")
    return R_orim1d(f"→{ps}{ch}", f"{ps}", f"{ch}", f"{ph}", s8)

@Theorem(3, "pm2.36")
def R_pm2_36(ph, ps, ch):
    s14 = R_pm1_4(f"{ph}", f"{ps}")
    s18 = R_pm2_38(f"{ph}", f"{ps}", f"{ch}")
    return R_syl5(f"∨{ph}{ps}", f"∨{ps}{ph}", f"→{ps}{ch}", f"∨{ch}{ph}", s14, s18)

@Theorem(3, "pm2.37")
def R_pm2_37(ph, ps, ch):
    s15 = R_pm2_38(f"{ph}", f"{ps}", f"{ch}")
    s18 = R_pm1_4(f"{ch}", f"{ph}")
    return R_syl6(f"→{ps}{ch}", f"∨{ps}{ph}", f"∨{ch}{ph}", f"∨{ph}{ch}", s15, s18)

@Theorem(4, "pm2.81")
def R_pm2_81(ph, ps, ch, th):
    s22 = R_orim2(f"{ph}", f"{ps}", f"→{ch}{th}")
    s26 = R_pm2_76(f"{ph}", f"{ch}", f"{th}")
    return R_syl6(f"→{ps}→{ch}{th}", f"∨{ph}{ps}", f"∨{ph}→{ch}{th}", f"→∨{ph}{ch}∨{ph}{th}", s22, s26)

@Theorem(3, "pm2.8")
def R_pm2_8(ph, ps, ch):
    s13 = R_pm2_53(f"{ph}", f"{ps}")
    s14 = R_con1d(f"∨{ph}{ps}", f"{ph}", f"{ps}", s13)
    return R_orim1d(f"∨{ph}{ps}", f"¬{ps}", f"{ph}", f"{ch}", s14)

@Theorem(3, "pm2.73")
def R_pm2_73(ph, ps, ch):
    s10 = R_pm2_621(f"{ph}", f"{ps}")
    return R_orim1d(f"→{ph}{ps}", f"∨{ph}{ps}", f"{ps}", f"{ch}", s10)

@Theorem(3, "pm2.74")
def R_pm2_74(ph, ps, ch):
    s16 = R_orel2(f"{ps}", f"{ph}")
    s19 = R_ax_1(f"{ph}", f"∨{ph}{ps}")
    s20 = R_ja(f"{ps}", f"{ph}", f"→∨{ph}{ps}{ph}", s16, s19)
    return R_orim1d(f"→{ps}{ph}", f"∨{ph}{ps}", f"{ph}", f"{ch}", s20)

@Theorem(4, "pm2.82")
def R_pm2_82(ph, ps, ch, th):
    s23 = R_pm2_24(f"{ch}", f"{ps}")
    s24 = R_orim2d(f"{ch}", f"¬{ch}", f"{ps}", f"{ph}", s23)
    s25 = R_jao1i(f"∨{ph}{ps}", f"{ch}", f"∨{ph}¬{ch}", s24)
    return R_orim1d(f"∨∨{ph}{ps}{ch}", f"∨{ph}¬{ch}", f"∨{ph}{ps}", f"{th}", s25)

@Theorem(4, "pm4.39")
def R_pm4_39(ph, ps, ch, th):
    s15 = R_simpl(f"↔{ph}{ch}", f"↔{ps}{th}")
    s18 = R_simpr(f"↔{ph}{ch}", f"↔{ps}{th}")
    return R_orbi12d(f"∧↔{ph}{ch}↔{ps}{th}", f"{ph}", f"{ch}", f"{ps}", f"{th}", s15, s18)

@Theorem(3, "animorl")
def R_animorl(ph, ps, ch):
    s7 = R_simpl(f"{ph}", f"{ps}")
    return R_orcd(f"∧{ph}{ps}", f"{ph}", f"{ch}", s7)

@Theorem(3, "animorr")
def R_animorr(ph, ps, ch):
    s7 = R_simpr(f"{ph}", f"{ps}")
    return R_olcd(f"∧{ph}{ps}", f"{ps}", f"{ch}", s7)

@Theorem(3, "animorlr")
def R_animorlr(ph, ps, ch):
    s7 = R_simpl(f"{ph}", f"{ps}")
    return R_olcd(f"∧{ph}{ps}", f"{ph}", f"{ch}", s7)

@Theorem(3, "animorrl")
def R_animorrl(ph, ps, ch):
    s7 = R_simpr(f"{ph}", f"{ps}")
    return R_orcd(f"∧{ph}{ps}", f"{ps}", f"{ch}", s7)

@Theorem(2, "ianor")
def R_ianor(ph, ps):
    s15 = R_imnan(f"{ph}", f"{ps}")
    s18 = R_pm4_62(f"{ph}", f"{ps}")
    return R_bitr3i(f"¬∧{ph}{ps}", f"→{ph}¬{ps}", f"∨¬{ph}¬{ps}", s15, s18)

@Theorem(2, "anor")
def R_anor(ph, ps):
    s12 = R_notnotb(f"∧{ph}{ps}")
    s15 = R_ianor(f"{ph}", f"{ps}")
    return R_xchbinx(f"∧{ph}{ps}", f"¬∧{ph}{ps}", f"∨¬{ph}¬{ps}", s12, s15)

@Theorem(2, "ioran")
def R_ioran(ph, ps):
    s14 = R_pm4_65(f"{ph}", f"{ps}")
    s17 = R_pm4_64(f"{ph}", f"{ps}")
    return R_xchnxbi(f"→¬{ph}{ps}", f"∧¬{ph}¬{ps}", f"∨{ph}{ps}", s14, s17)

@Theorem(2, "pm4.52")
def R_pm4_52(ph, ps):
    s13 = R_annim(f"{ph}", f"{ps}")
    s16 = R_imor(f"{ph}", f"{ps}")
    return R_xchbinx(f"∧{ph}¬{ps}", f"→{ph}{ps}", f"∨¬{ph}{ps}", s13, s16)

@Theorem(2, "pm4.53")
def R_pm4_53(ph, ps):
    s15 = R_pm4_52(f"{ph}", f"{ps}")
    s16 = R_con2bii(f"∧{ph}¬{ps}", f"∨¬{ph}{ps}", s15)
    return R_bicomi(f"∨¬{ph}{ps}", f"¬∧{ph}¬{ps}", s16)

@Theorem(2, "pm4.54")
def R_pm4_54(ph, ps):
    s15 = R_df_an(f"¬{ph}", f"{ps}")
    s18 = R_pm4_66(f"{ph}", f"{ps}")
    return R_xchbinx(f"∧¬{ph}{ps}", f"→¬{ph}¬{ps}", f"∨{ph}¬{ps}", s15, s18)

@Theorem(2, "pm4.55")
def R_pm4_55(ph, ps):
    s15 = R_pm4_54(f"{ph}", f"{ps}")
    s16 = R_con2bii(f"∧¬{ph}{ps}", f"∨{ph}¬{ps}", s15)
    return R_bicomi(f"∨{ph}¬{ps}", f"¬∧¬{ph}{ps}", s16)

@Theorem(2, "pm4.56")
def R_pm4_56(ph, ps):
    s11 = R_ioran(f"{ph}", f"{ps}")
    return R_bicomi(f"¬∨{ph}{ps}", f"∧¬{ph}¬{ps}", s11)

@Theorem(2, "oran")
def R_oran(ph, ps):
    s10 = R_pm4_56(f"{ph}", f"{ps}")
    return R_con2bii(f"∧¬{ph}¬{ps}", f"∨{ph}{ps}", s10)

@Theorem(2, "pm4.57")
def R_pm4_57(ph, ps):
    s11 = R_oran(f"{ph}", f"{ps}")
    return R_bicomi(f"∨{ph}{ps}", f"¬∧¬{ph}¬{ps}", s11)

@Theorem(2, "pm3.1")
def R_pm3_1(ph, ps):
    s11 = R_anor(f"{ph}", f"{ps}")
    return R_biimpi(f"∧{ph}{ps}", f"¬∨¬{ph}¬{ps}", s11)

@Theorem(2, "pm3.11")
def R_pm3_11(ph, ps):
    s11 = R_anor(f"{ph}", f"{ps}")
    return R_biimpri(f"∧{ph}{ps}", f"¬∨¬{ph}¬{ps}", s11)

@Theorem(2, "pm3.12")
def R_pm3_12(ph, ps):
    s10 = R_pm3_11(f"{ph}", f"{ps}")
    return R_orri(f"∨¬{ph}¬{ps}", f"∧{ph}{ps}", s10)

@Theorem(2, "pm3.13")
def R_pm3_13(ph, ps):
    s10 = R_pm3_11(f"{ph}", f"{ps}")
    return R_con1i(f"∨¬{ph}¬{ps}", f"∧{ph}{ps}", s10)

@Theorem(2, "pm3.14")
def R_pm3_14(ph, ps):
    s10 = R_pm3_1(f"{ph}", f"{ps}")
    return R_con2i(f"∧{ph}{ps}", f"∨¬{ph}¬{ps}", s10)

@Theorem(2, "pm4.44")
def R_pm4_44(ph, ps):
    s9 = R_orc(f"{ph}", f"∧{ph}{ps}")
    s14 = R_id(f"{ph}")
    s17 = R_simpl(f"{ph}", f"{ps}")
    s18 = R_jaoi(f"{ph}", f"{ph}", f"∧{ph}{ps}", s14, s17)
    return R_impbii(f"{ph}", f"∨{ph}∧{ph}{ps}", s9, s18)

@Theorem(2, "pm4.45")
def R_pm4_45(ph, ps):
    s6 = R_orc(f"{ph}", f"{ps}")
    return R_pm4_71i(f"{ph}", f"∨{ph}{ps}", s6)

@Theorem(2, "orabs")
def R_orabs(ph, ps):
    s6 = R_orc(f"{ph}", f"{ps}")
    return R_pm4_71ri(f"{ph}", f"∨{ph}{ps}", s6)

@Theorem(2, "oranabs")
def R_oranabs(ph, ps):
    s16 = R_biortn(f"{ps}", f"{ph}")
    s19 = R_orcom(f"¬{ps}", f"{ph}")
    s20 = R_bitr2di(f"{ps}", f"{ph}", f"∨¬{ps}{ph}", f"∨{ph}¬{ps}", s16, s19)
    return R_pm5_32ri(f"{ps}", f"∨{ph}¬{ps}", f"{ph}", s20)

@Theorem(2, "pm5.61")
def R_pm5_61(ph, ps):
    s13 = R_orel2(f"{ps}", f"{ph}")
    s16 = R_orc(f"{ph}", f"{ps}")
    s17 = R_impbid1(f"¬{ps}", f"∨{ph}{ps}", f"{ph}", s13, s16)
    return R_pm5_32ri(f"¬{ps}", f"∨{ph}{ps}", f"{ph}", s17)

@Theorem(3, "pm5.6")
def R_pm5_6(ph, ps, ch):
    s22 = R_impexp(f"{ph}", f"¬{ps}", f"{ch}")
    s28 = R_df_or(f"{ps}", f"{ch}")
    s29 = R_imbi2i(f"∨{ps}{ch}", f"→¬{ps}{ch}", f"{ph}", s28)
    return R_bitr4i(f"→∧{ph}¬{ps}{ch}", f"→{ph}→¬{ps}{ch}", f"→{ph}∨{ps}{ch}", s22, s29)

def R_orcanai(ph, ps, ch, h1):
    s8 = R_ord(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_imp(f"{ph}", f"¬{ps}", f"{ch}", s8)

@Theorem(3, "pm4.79")
def R_pm4_79(ph, ps, ch):
    s21 = R_id(f"→{ps}{ph}")
    s23 = R_id(f"→{ch}{ph}")
    s24 = R_jaoa(f"→{ps}{ph}", f"{ps}", f"{ph}", f"→{ch}{ph}", f"{ch}", s21, s23)
    s35 = R_simplim(f"{ps}", f"{ph}")
    s39 = R_pm3_3(f"{ps}", f"{ch}", f"{ph}")
    s40 = R_syl5(f"¬→{ps}{ph}", f"{ps}", f"→∧{ps}{ch}{ph}", f"→{ch}{ph}", s35, s39)
    s41 = R_orrd(f"→∧{ps}{ch}{ph}", f"→{ps}{ph}", f"→{ch}{ph}", s40)
    return R_impbii(f"∨→{ps}{ph}→{ch}{ph}", f"→∧{ps}{ch}{ph}", s24, s41)

@Theorem(4, "pm5.53")
def R_pm5_53(ph, ps, ch, th):
    s24 = R_jaob(f"∨{ph}{ps}", f"{th}", f"{ch}")
    s28 = R_jaob(f"{ph}", f"{th}", f"{ps}")
    return R_bianbi(f"→∨∨{ph}{ps}{ch}{th}", f"→∨{ph}{ps}{th}", f"→{ch}{th}", f"∧→{ph}{th}→{ps}{th}", s24, s28)

@Theorem(3, "ordi")
def R_ordi(ph, ps, ch):
    s32 = R_jcab(f"¬{ph}", f"{ps}", f"{ch}")
    s35 = R_df_or(f"{ph}", f"∧{ps}{ch}")
    s42 = R_df_or(f"{ph}", f"{ps}")
    s45 = R_df_or(f"{ph}", f"{ch}")
    s46 = R_anbi12i(f"∨{ph}{ps}", f"→¬{ph}{ps}", f"∨{ph}{ch}", f"→¬{ph}{ch}", s42, s45)
    return R_3bitr4i(f"→¬{ph}∧{ps}{ch}", f"∧→¬{ph}{ps}→¬{ph}{ch}", f"∨{ph}∧{ps}{ch}", f"∧∨{ph}{ps}∨{ph}{ch}", s32, s35, s46)

@Theorem(3, "ordir")
def R_ordir(ph, ps, ch):
    s30 = R_ordi(f"{ch}", f"{ph}", f"{ps}")
    s33 = R_orcom(f"∧{ph}{ps}", f"{ch}")
    s40 = R_orcom(f"{ph}", f"{ch}")
    s43 = R_orcom(f"{ps}", f"{ch}")
    s44 = R_anbi12i(f"∨{ph}{ch}", f"∨{ch}{ph}", f"∨{ps}{ch}", f"∨{ch}{ps}", s40, s43)
    return R_3bitr4i(f"∨{ch}∧{ph}{ps}", f"∧∨{ch}{ph}∨{ch}{ps}", f"∨∧{ph}{ps}{ch}", f"∧∨{ph}{ch}∨{ps}{ch}", s30, s33, s44)

@Theorem(3, "andi")
def R_andi(ph, ps, ch):
    s23 = R_orc(f"∧{ph}{ps}", f"∧{ph}{ch}")
    s26 = R_olc(f"∧{ph}{ch}", f"∧{ph}{ps}")
    s27 = R_jaodan(f"{ph}", f"{ps}", f"∨∧{ph}{ps}∧{ph}{ch}", f"{ch}", s23, s26)
    s36 = R_orc(f"{ps}", f"{ch}")
    s37 = R_anim2i(f"{ps}", f"∨{ps}{ch}", f"{ph}", s36)
    s43 = R_olc(f"{ch}", f"{ps}")
    s44 = R_anim2i(f"{ch}", f"∨{ps}{ch}", f"{ph}", s43)
    s45 = R_jaoi(f"∧{ph}{ps}", f"∧{ph}∨{ps}{ch}", f"∧{ph}{ch}", s37, s44)
    return R_impbii(f"∧{ph}∨{ps}{ch}", f"∨∧{ph}{ps}∧{ph}{ch}", s27, s45)

@Theorem(3, "andir")
def R_andir(ph, ps, ch):
    s30 = R_andi(f"{ch}", f"{ph}", f"{ps}")
    s33 = R_ancom(f"∨{ph}{ps}", f"{ch}")
    s40 = R_ancom(f"{ph}", f"{ch}")
    s43 = R_ancom(f"{ps}", f"{ch}")
    s44 = R_orbi12i(f"∧{ph}{ch}", f"∧{ch}{ph}", f"∧{ps}{ch}", f"∧{ch}{ps}", s40, s43)
    return R_3bitr4i(f"∧{ch}∨{ph}{ps}", f"∨∧{ch}{ph}∧{ch}{ps}", f"∧∨{ph}{ps}{ch}", f"∨∧{ph}{ch}∧{ps}{ch}", s30, s33, s44)

@Theorem(4, "orddi")
def R_orddi(ph, ps, ch, th):
    s37 = R_ordir(f"{ph}", f"{ps}", f"∧{ch}{th}")
    s45 = R_ordi(f"{ph}", f"{ch}", f"{th}")
    s49 = R_ordi(f"{ps}", f"{ch}", f"{th}")
    s50 = R_anbi12i(f"∨{ph}∧{ch}{th}", f"∧∨{ph}{ch}∨{ph}{th}", f"∨{ps}∧{ch}{th}", f"∧∨{ps}{ch}∨{ps}{th}", s45, s49)
    return R_bitri(f"∨∧{ph}{ps}∧{ch}{th}", f"∧∨{ph}∧{ch}{th}∨{ps}∧{ch}{th}", f"∧∧∨{ph}{ch}∨{ph}{th}∧∨{ps}{ch}∨{ps}{th}", s37, s50)

@Theorem(4, "anddi")
def R_anddi(ph, ps, ch, th):
    s37 = R_andir(f"{ph}", f"{ps}", f"∨{ch}{th}")
    s45 = R_andi(f"{ph}", f"{ch}", f"{th}")
    s49 = R_andi(f"{ps}", f"{ch}", f"{th}")
    s50 = R_orbi12i(f"∧{ph}∨{ch}{th}", f"∨∧{ph}{ch}∧{ph}{th}", f"∧{ps}∨{ch}{th}", f"∨∧{ps}{ch}∧{ps}{th}", s45, s49)
    return R_bitri(f"∧∨{ph}{ps}∨{ch}{th}", f"∨∧{ph}∨{ch}{th}∧{ps}∨{ch}{th}", f"∨∨∧{ph}{ch}∧{ph}{th}∨∧{ps}{ch}∧{ps}{th}", s37, s50)

@Theorem(2, "pm5.17")
def R_pm5_17(ph, ps):
    s29 = R_bicom(f"{ph}", f"¬{ps}")
    s32 = R_dfbi2(f"¬{ps}", f"{ph}")
    s44 = R_orcom(f"{ph}", f"{ps}")
    s47 = R_df_or(f"{ps}", f"{ph}")
    s48 = R_bitr2i(f"∨{ph}{ps}", f"∨{ps}{ph}", f"→¬{ps}{ph}", s44, s47)
    s51 = R_imnan(f"{ph}", f"{ps}")
    s52 = R_anbi12i(f"→¬{ps}{ph}", f"∨{ph}{ps}", f"→{ph}¬{ps}", f"¬∧{ph}{ps}", s48, s51)
    return R_3bitrri(f"↔{ph}¬{ps}", f"↔¬{ps}{ph}", f"∧→¬{ps}{ph}→{ph}¬{ps}", f"∧∨{ph}{ps}¬∧{ph}{ps}", s29, s32, s52)

@Theorem(2, "pm5.15")
def R_pm5_15(ph, ps):
    s14 = R_xor3(f"{ph}", f"{ps}")
    s15 = R_biimpi(f"¬↔{ph}{ps}", f"↔{ph}¬{ps}", s14)
    return R_orri(f"↔{ph}{ps}", f"↔{ph}¬{ps}", s15)

@Theorem(2, "pm5.16")
def R_pm5_16(ph, ps):
    s20 = R_pm5_18(f"{ph}", f"{ps}")
    s21 = R_biimpi(f"↔{ph}{ps}", f"¬↔{ph}¬{ps}", s20)
    s24 = R_imnan(f"↔{ph}{ps}", f"↔{ph}¬{ps}")
    return R_mpbi(f"→↔{ph}{ps}¬↔{ph}¬{ps}", f"¬∧↔{ph}{ps}↔{ph}¬{ps}", s21, s24)

@Theorem(2, "xor")
def R_xor(ph, ps):
    s41 = R_iman(f"{ph}", f"{ps}")
    s44 = R_iman(f"{ps}", f"{ph}")
    s45 = R_anbi12i(f"→{ph}{ps}", f"¬∧{ph}¬{ps}", f"→{ps}{ph}", f"¬∧{ps}¬{ph}", s41, s44)
    s48 = R_dfbi2(f"{ph}", f"{ps}")
    s51 = R_ioran(f"∧{ph}¬{ps}", f"∧{ps}¬{ph}")
    s52 = R_3bitr4ri(f"∧→{ph}{ps}→{ps}{ph}", f"∧¬∧{ph}¬{ps}¬∧{ps}¬{ph}", f"↔{ph}{ps}", f"¬∨∧{ph}¬{ps}∧{ps}¬{ph}", s45, s48, s51)
    return R_con1bii(f"∨∧{ph}¬{ps}∧{ps}¬{ph}", f"↔{ph}{ps}", s52)

@Theorem(2, "nbi2")
def R_nbi2(ph, ps):
    s18 = R_xor3(f"{ph}", f"{ps}")
    s21 = R_pm5_17(f"{ph}", f"{ps}")
    return R_bitr4i(f"¬↔{ph}{ps}", f"↔{ph}¬{ps}", f"∧∨{ph}{ps}¬∧{ph}{ps}", s18, s21)

@Theorem(3, "xordi")
def R_xordi(ph, ps, ch):
    s19 = R_annim(f"{ph}", f"↔{ps}{ch}")
    s23 = R_pm5_32(f"{ph}", f"{ps}", f"{ch}")
    return R_xchbinx(f"∧{ph}¬↔{ps}{ch}", f"→{ph}↔{ps}{ch}", f"↔∧{ph}{ps}∧{ph}{ch}", s19, s23)

@Theorem(2, "pm5.54")
def R_pm5_54(ph, ps):
    s21 = R_iba(f"{ps}", f"{ph}")
    s22 = R_bicomd(f"{ps}", f"{ph}", f"∧{ph}{ps}", s21)
    s24 = R_adantl(f"{ps}", f"↔∧{ph}{ps}{ph}", f"{ph}", s22)
    s26 = R_pm5_21ni(f"∧{ph}{ps}", f"↔∧{ph}{ps}{ph}", f"{ps}", s24, s22)
    return R_orri(f"↔∧{ph}{ps}{ph}", f"↔∧{ph}{ps}{ps}", s26)

@Theorem(2, "pm5.62")
def R_pm5_62(ph, ps):
    s14 = R_exmid(f"{ps}")
    s18 = R_ordir(f"{ph}", f"{ps}", f"¬{ps}")
    return R_mpbiran2(f"∨∧{ph}{ps}¬{ps}", f"∨{ph}¬{ps}", f"∨{ps}¬{ps}", s14, s18)

@Theorem(2, "pm5.63")
def R_pm5_63(ph, ps):
    s18 = R_exmid(f"{ph}")
    s22 = R_ordi(f"{ph}", f"¬{ph}", f"{ps}")
    s23 = R_mpbiran(f"∨{ph}∧¬{ph}{ps}", f"∨{ph}¬{ph}", f"∨{ph}{ps}", s18, s22)
    return R_bicomi(f"∨{ph}∧¬{ph}{ps}", f"∨{ph}{ps}", s23)

def R_niabn(ph, ps, ch, h1):
    s8 = R_simpr(f"{ch}", f"{ps}")
    s12 = R_pm2_24i(f"{ph}", f"{ps}", h1)
    return R_pm5_21ni(f"∧{ch}{ps}", f"{ps}", f"¬{ph}", s8, s12)

def R_ninba(ph, ps, ch, h1):
    s11 = R_niabn(f"{ph}", f"{ps}", f"{ch}", h1)
    return R_bicomd(f"¬{ps}", f"∧{ch}{ps}", f"¬{ph}", s11)

@Theorem(2, "pm4.43")
def R_pm4_43(ph, ps):
    s19 = R_pm3_24(f"{ps}")
    s20 = R_biorfri(f"∧{ps}¬{ps}", f"{ph}", s19)
    s24 = R_ordi(f"{ph}", f"{ps}", f"¬{ps}")
    return R_bitri(f"{ph}", f"∨{ph}∧{ps}¬{ps}", f"∧∨{ph}{ps}∨{ph}¬{ps}", s20, s24)

@Theorem(2, "pm4.82")
def R_pm4_82(ph, ps):
    s19 = R_pm2_65(f"{ph}", f"{ps}")
    s20 = R_imp(f"→{ph}{ps}", f"→{ph}¬{ps}", f"¬{ph}", s19)
    s26 = R_pm2_21(f"{ph}", f"{ps}")
    s29 = R_pm2_21(f"{ph}", f"¬{ps}")
    s30 = R_jca(f"¬{ph}", f"→{ph}{ps}", f"→{ph}¬{ps}", s26, s29)
    return R_impbii(f"∧→{ph}{ps}→{ph}¬{ps}", f"¬{ph}", s20, s30)

@Theorem(2, "pm4.83")
def R_pm4_83(ph, ps):
    s19 = R_exmid(f"{ph}")
    s20 = R_a1bi(f"∨{ph}¬{ph}", f"{ps}", s19)
    s24 = R_jaob(f"{ph}", f"{ps}", f"¬{ph}")
    return R_bitr2i(f"{ps}", f"→∨{ph}¬{ph}{ps}", f"∧→{ph}{ps}→¬{ph}{ps}", s20, s24)

@Theorem(2, "pclem6")
def R_pclem6(ph, ps):
    s18 = R_ibar(f"{ps}", f"¬{ph}")
    s21 = R_nbbn(f"{ph}", f"∧{ps}¬{ph}")
    s22 = R_sylib(f"{ps}", f"↔¬{ph}∧{ps}¬{ph}", f"¬↔{ph}∧{ps}¬{ph}", s18, s21)
    return R_con2i(f"{ps}", f"↔{ph}∧{ps}¬{ph}", s22)

@Theorem(2, "bigolden")
def R_bigolden(ph, ps):
    s19 = R_pm4_71(f"{ph}", f"{ps}")
    s22 = R_pm4_72(f"{ph}", f"{ps}")
    s25 = R_bicom(f"{ph}", f"∧{ph}{ps}")
    return R_3bitr3ri(f"→{ph}{ps}", f"↔{ph}∧{ph}{ps}", f"↔{ps}∨{ph}{ps}", f"↔∧{ph}{ps}{ph}", s19, s22, s25)

@Theorem(3, "pm5.71")
def R_pm5_71(ph, ps, ch):
    s25 = R_orel2(f"{ps}", f"{ph}")
    s28 = R_orc(f"{ph}", f"{ps}")
    s29 = R_impbid1(f"¬{ps}", f"∨{ph}{ps}", f"{ph}", s25, s28)
    s30 = R_anbi1d(f"¬{ps}", f"∨{ph}{ps}", f"{ph}", f"{ch}", s29)
    s39 = R_pm2_21(f"{ch}", f"↔∨{ph}{ps}{ph}")
    s40 = R_pm5_32rd(f"¬{ch}", f"{ch}", f"∨{ph}{ps}", f"{ph}", s39)
    return R_ja(f"{ps}", f"¬{ch}", f"↔∧∨{ph}{ps}{ch}∧{ph}{ch}", s30, s40)

@Theorem(3, "pm5.75")
def R_pm5_75(ph, ps, ch):
    s31 = R_anbi1(f"{ph}", f"∨{ps}{ch}", f"¬{ps}")
    s40 = R_biorf(f"{ps}", f"{ch}")
    s41 = R_bicomd(f"¬{ps}", f"{ch}", f"∨{ps}{ch}", s40)
    s42 = R_pm5_32ri(f"¬{ps}", f"∨{ps}{ch}", f"{ch}", s41)
    s43 = R_bitrdi(f"↔{ph}∨{ps}{ch}", f"∧{ph}¬{ps}", f"∧∨{ps}{ch}¬{ps}", f"∧{ch}¬{ps}", s31, s42)
    s49 = R_abai(f"{ch}", f"¬{ps}")
    s50 = R_rbaib(f"∧{ch}¬{ps}", f"{ch}", f"→{ch}¬{ps}", s49)
    return R_sylan9bbr(f"↔{ph}∨{ps}{ch}", f"∧{ph}¬{ps}", f"∧{ch}¬{ps}", f"→{ch}¬{ps}", f"{ch}", s43, s50)

def R_ecase2d(ph, ps, ch, th, ta, h1, h2, h3, h4):
    s12 = R_mpnanrd(f"{ph}", f"{ps}", f"{ch}", h1, h2)
    s18 = R_mpnanrd(f"{ph}", f"{ps}", f"{th}", h1, h3)
    s25 = R_ord(f"{ph}", f"{ta}", f"∨{ch}{th}", h4)
    s26 = R_mtord(f"{ph}", f"¬{ta}", f"{ch}", f"{th}", s12, s18, s25)
    return R_notnotrd(f"{ph}", f"{ta}", s26)

def R_ecase2dOLD(ph, ps, ch, th, ta, h1, h2, h3, h4):
    s8 = R_idd(f"{ph}", f"{ta}")
    s24 = R_pm2_21d(f"{ph}", f"∧{ps}{ch}", f"{ta}", h2)
    s25 = R_mpand(f"{ph}", f"{ps}", f"{ch}", f"{ta}", h1, s24)
    s37 = R_pm2_21d(f"{ph}", f"∧{ps}{th}", f"{ta}", h3)
    s38 = R_mpand(f"{ph}", f"{ps}", f"{th}", f"{ta}", h1, s37)
    s39 = R_jaod(f"{ph}", f"{ch}", f"{ta}", f"{th}", s25, s38)
    return R_mpjaod(f"{ph}", f"{ta}", f"{ta}", f"∨{ch}{th}", s8, s39, h4)

def R_ecase3(ph, ps, ch, h1, h2, h3):
    s9 = R_jaoi(f"{ph}", f"{ch}", f"{ps}", h1, h2)
    return R_pm2_61i(f"∨{ph}{ps}", f"{ch}", s9, h3)

def R_ecase(ph, ps, ch, h1, h2, h3):
    s7 = R_ex(f"{ph}", f"{ps}", f"{ch}", h3)
    return R_pm2_61nii(f"{ph}", f"{ps}", f"{ch}", s7, h1, h2)

def R_ecase3d(ph, ps, ch, th, h1, h2, h3):
    s11 = R_jaod(f"{ph}", f"{ps}", f"{th}", f"{ch}", h1, h2)
    return R_pm2_61d(f"{ph}", f"∨{ps}{ch}", f"{th}", s11, h3)

def R_ecased(ph, ps, ch, th, h1, h2, h3):
    s21 = R_pm3_11(f"{ps}", f"{ch}")
    s23 = R_syl5(f"¬∨¬{ps}¬{ch}", f"∧{ps}{ch}", f"{ph}", f"{th}", s21, h3)
    return R_ecase3d(f"{ph}", f"¬{ps}", f"¬{ch}", f"{th}", h1, h2, s23)

def R_ecase3ad(ph, ps, ch, th, h1, h2, h3):
    s8 = R_imp(f"{ph}", f"{ps}", f"{th}", h1)
    s13 = R_imp(f"{ph}", f"{ch}", f"{th}", h2)
    s22 = R_imp(f"{ph}", f"∧¬{ps}¬{ch}", f"{th}", h3)
    return R_pm2_61ddan(f"{ph}", f"{ps}", f"{ch}", f"{th}", s8, s13, s22)

def R_ecase3adOLD(ph, ps, ch, th, h1, h2, h3):
    s14 = R_notnotr(f"{ps}")
    s16 = R_syl5(f"¬¬{ps}", f"{ps}", f"{ph}", f"{th}", s14, h1)
    s23 = R_notnotr(f"{ch}")
    s25 = R_syl5(f"¬¬{ch}", f"{ch}", f"{ph}", f"{th}", s23, h2)
    return R_ecased(f"{ph}", f"¬{ps}", f"¬{ch}", f"{th}", s16, s25, h3)

def R_ccase(ph, ps, ch, th, ta, h1, h2, h3, h4):
    s12 = R_jaoian(f"{ph}", f"{ps}", f"{ta}", f"{ch}", h1, h2)
    s19 = R_jaoian(f"{ph}", f"{th}", f"{ta}", f"{ch}", h3, h4)
    return R_jaodan(f"∨{ph}{ch}", f"{ps}", f"{ta}", f"{th}", s12, s19)

def R_ccased(ph, ps, ch, th, ta, et, h1, h2, h3, h4):
    s22 = R_com12(f"{ph}", f"∧{ps}{ch}", f"{et}", h1)
    s29 = R_com12(f"{ph}", f"∧{th}{ch}", f"{et}", h2)
    s36 = R_com12(f"{ph}", f"∧{ps}{ta}", f"{et}", h3)
    s43 = R_com12(f"{ph}", f"∧{th}{ta}", f"{et}", h4)
    s44 = R_ccase(f"{ps}", f"{ch}", f"{th}", f"{ta}", f"→{ph}{et}", s22, s29, s36, s43)
    return R_com12(f"∧∨{ps}{th}∨{ch}{ta}", f"{ph}", f"{et}", s44)

def R_ccase2(ph, ps, ch, th, ta, h1, h2, h3):
    s10 = R_adantr(f"{ch}", f"{ta}", f"{ps}", h2)
    s15 = R_adantl(f"{th}", f"{ta}", f"{ph}", h3)
    s20 = R_adantl(f"{th}", f"{ta}", f"{ch}", h3)
    return R_ccase(f"{ph}", f"{ps}", f"{ch}", f"{th}", f"{ta}", h1, s10, s15, s20)

def R_4cases(ph, ps, ch, h1, h2, h3, h4):
    s7 = R_pm2_61ian(f"{ph}", f"{ps}", f"{ch}", h1, h3)
    s14 = R_pm2_61ian(f"{ph}", f"¬{ps}", f"{ch}", h2, h4)
    return R_pm2_61i(f"{ps}", f"{ch}", s7, s14)

def R_4casesdan(ph, ps, ch, th, h1, h2, h3, h4):
    s11 = R_expcom(f"{ph}", f"∧{ps}{ch}", f"{th}", h1)
    s20 = R_expcom(f"{ph}", f"∧{ps}¬{ch}", f"{th}", h2)
    s29 = R_expcom(f"{ph}", f"∧¬{ps}{ch}", f"{th}", h3)
    s36 = R_expcom(f"{ph}", f"∧¬{ps}¬{ch}", f"{th}", h4)
    return R_4cases(f"{ps}", f"{ch}", f"→{ph}{th}", s11, s20, s29, s36)

def R_cases(ph, ps, ch, th, h1, h2):
    s30 = R_exmid(f"{ph}")
    s31 = R_biantrur(f"∨{ph}¬{ph}", f"{ps}", s30)
    s35 = R_andir(f"{ph}", f"¬{ph}", f"{ps}")
    s44 = R_pm5_32i(f"{ph}", f"{ps}", f"{ch}", h1)
    s49 = R_pm5_32i(f"¬{ph}", f"{ps}", f"{th}", h2)
    s50 = R_orbi12i(f"∧{ph}{ps}", f"∧{ph}{ch}", f"∧¬{ph}{ps}", f"∧¬{ph}{th}", s44, s49)
    return R_3bitri(f"{ps}", f"∧∨{ph}¬{ph}{ps}", f"∨∧{ph}{ps}∧¬{ph}{ps}", f"∨∧{ph}{ch}∧¬{ph}{th}", s31, s35, s50)

@Theorem(3, "dedlem0a")
def R_dedlem0a(ph, ps, ch):
    s15 = R_iba(f"{ph}", f"{ps}")
    s23 = R_biimt(f"→{ch}{ph}", f"∧{ps}{ph}")
    s24 = R_jarri(f"{ch}", f"{ph}", f"↔∧{ps}{ph}→→{ch}{ph}∧{ps}{ph}", s23)
    return R_bitrd(f"{ph}", f"{ps}", f"∧{ps}{ph}", f"→→{ch}{ph}∧{ps}{ph}", s15, s24)

@Theorem(3, "dedlem0b")
def R_dedlem0b(ph, ps, ch):
    s24 = R_pm2_21(f"{ph}", f"∧{ch}{ph}")
    s25 = R_imim2d(f"¬{ph}", f"{ph}", f"∧{ch}{ph}", f"{ps}", s24)
    s26 = R_com23(f"¬{ph}", f"→{ps}{ph}", f"{ps}", f"∧{ch}{ph}", s25)
    s40 = R_pm2_21(f"{ps}", f"{ph}")
    s43 = R_simpr(f"{ch}", f"{ph}")
    s44 = R_imim12i(f"¬{ps}", f"→{ps}{ph}", f"∧{ch}{ph}", f"{ph}", s40, s43)
    s45 = R_con1d(f"→→{ps}{ph}∧{ch}{ph}", f"{ps}", f"{ph}", s44)
    s46 = R_com12(f"→→{ps}{ph}∧{ch}{ph}", f"¬{ph}", f"{ps}", s45)
    return R_impbid(f"¬{ph}", f"{ps}", f"→→{ps}{ph}∧{ch}{ph}", s26, s46)

@Theorem(3, "dedlema")
def R_dedlema(ph, ps, ch):
    s19 = R_orc(f"∧{ps}{ph}", f"∧{ch}¬{ph}")
    s20 = R_expcom(f"{ps}", f"{ph}", f"∨∧{ps}{ph}∧{ch}¬{ph}", s19)
    s31 = R_simpl(f"{ps}", f"{ph}")
    s32 = R_a1i(f"→∧{ps}{ph}{ps}", f"{ph}", s31)
    s39 = R_pm2_24(f"{ph}", f"{ps}")
    s40 = R_adantld(f"{ph}", f"¬{ph}", f"{ps}", f"{ch}", s39)
    s41 = R_jaod(f"{ph}", f"∧{ps}{ph}", f"{ps}", f"∧{ch}¬{ph}", s32, s40)
    return R_impbid(f"{ph}", f"{ps}", f"∨∧{ps}{ph}∧{ch}¬{ph}", s20, s41)

@Theorem(3, "dedlemb")
def R_dedlemb(ph, ps, ch):
    s19 = R_olc(f"∧{ch}¬{ph}", f"∧{ps}{ph}")
    s20 = R_expcom(f"{ch}", f"¬{ph}", f"∨∧{ps}{ph}∧{ch}¬{ph}", s19)
    s31 = R_pm2_21(f"{ph}", f"{ch}")
    s32 = R_adantld(f"¬{ph}", f"{ph}", f"{ch}", f"{ps}", s31)
    s39 = R_simpl(f"{ch}", f"¬{ph}")
    s40 = R_a1i(f"→∧{ch}¬{ph}{ch}", f"¬{ph}", s39)
    s41 = R_jaod(f"¬{ph}", f"∧{ps}{ph}", f"{ch}", f"∧{ch}¬{ph}", s32, s40)
    return R_impbid(f"¬{ph}", f"{ch}", f"∨∧{ps}{ph}∧{ch}¬{ph}", s20, s41)

@Theorem(3, "cases2")
def R_cases2(ph, ps, ch):
    s41 = R_pm4_83(f"{ph}", f"∨∧{ps}{ph}∧{ch}¬{ph}")
    s52 = R_dedlema(f"{ph}", f"{ps}", f"{ch}")
    s53 = R_pm5_74i(f"{ph}", f"{ps}", f"∨∧{ps}{ph}∧{ch}¬{ph}", s52)
    s60 = R_dedlemb(f"{ph}", f"{ps}", f"{ch}")
    s61 = R_pm5_74i(f"¬{ph}", f"{ch}", f"∨∧{ps}{ph}∧{ch}¬{ph}", s60)
    s62 = R_anbi12i(f"→{ph}{ps}", f"→{ph}∨∧{ps}{ph}∧{ch}¬{ph}", f"→¬{ph}{ch}", f"→¬{ph}∨∧{ps}{ph}∧{ch}¬{ph}", s53, s61)
    s69 = R_ancom(f"{ph}", f"{ps}")
    s72 = R_ancom(f"¬{ph}", f"{ch}")
    s73 = R_orbi12i(f"∧{ph}{ps}", f"∧{ps}{ph}", f"∧¬{ph}{ch}", f"∧{ch}¬{ph}", s69, s72)
    return R_3bitr4ri(f"∧→{ph}∨∧{ps}{ph}∧{ch}¬{ph}→¬{ph}∨∧{ps}{ph}∧{ch}¬{ph}", f"∨∧{ps}{ph}∧{ch}¬{ph}", f"∧→{ph}{ps}→¬{ph}{ch}", f"∨∧{ph}{ps}∧¬{ph}{ch}", s41, s62, s73)

@Theorem(2, "dfbi3")
def R_dfbi3(ph, ps):
    s34 = R_con34b(f"{ps}", f"{ph}")
    s35 = R_anbi2i(f"→{ps}{ph}", f"→¬{ph}¬{ps}", f"→{ph}{ps}", s34)
    s38 = R_dfbi2(f"{ph}", f"{ps}")
    s42 = R_cases2(f"{ph}", f"{ps}", f"¬{ps}")
    return R_3bitr4i(f"∧→{ph}{ps}→{ps}{ph}", f"∧→{ph}{ps}→¬{ph}¬{ps}", f"↔{ph}{ps}", f"∨∧{ph}{ps}∧¬{ph}¬{ps}", s35, s38, s42)

@Theorem(2, "pm5.24")
def R_pm5_24(ph, ps):
    s23 = R_xor(f"{ph}", f"{ps}")
    s26 = R_dfbi3(f"{ph}", f"{ps}")
    return R_xchnxbi(f"↔{ph}{ps}", f"∨∧{ph}¬{ps}∧{ps}¬{ph}", f"∨∧{ph}{ps}∧¬{ph}¬{ps}", s23, s26)

@Theorem(2, "4exmid")
def R_4exmid(ph, ps):
    s25 = R_pm5_24(f"{ph}", f"{ps}")
    s26 = R_biimpi(f"¬∨∧{ph}{ps}∧¬{ph}¬{ps}", f"∨∧{ph}¬{ps}∧{ps}¬{ph}", s25)
    return R_orri(f"∨∧{ph}{ps}∧¬{ph}¬{ps}", f"∨∧{ph}¬{ps}∧{ps}¬{ph}", s26)

@Theorem(3, "consensus")
def R_consensus(ph, ps, ch):
    s22 = R_id(f"∨∧{ph}{ps}∧¬{ph}{ch}")
    s32 = R_orc(f"∧{ph}{ps}", f"∧¬{ph}{ch}")
    s33 = R_adantrr(f"{ph}", f"{ps}", f"∨∧{ph}{ps}∧¬{ph}{ch}", f"{ch}", s32)
    s40 = R_olc(f"∧¬{ph}{ch}", f"∧{ph}{ps}")
    s41 = R_adantrl(f"¬{ph}", f"{ch}", f"∨∧{ph}{ps}∧¬{ph}{ch}", f"{ps}", s40)
    s42 = R_pm2_61ian(f"{ph}", f"∧{ps}{ch}", f"∨∧{ph}{ps}∧¬{ph}{ch}", s33, s41)
    s43 = R_jaoi(f"∨∧{ph}{ps}∧¬{ph}{ch}", f"∨∧{ph}{ps}∧¬{ph}{ch}", f"∧{ps}{ch}", s22, s42)
    s46 = R_orc(f"∨∧{ph}{ps}∧¬{ph}{ch}", f"∧{ps}{ch}")
    return R_impbii(f"∨∨∧{ph}{ps}∧¬{ph}{ch}∧{ps}{ch}", f"∨∧{ph}{ps}∧¬{ph}{ch}", s43, s46)

@Theorem(2, "pm4.42")
def R_pm4_42(ph, ps):
    s14 = R_dedlema(f"{ps}", f"{ph}", f"{ph}")
    s18 = R_dedlemb(f"{ps}", f"{ph}", f"{ph}")
    return R_pm2_61i(f"{ps}", f"↔{ph}∨∧{ph}{ps}∧{ph}¬{ps}", s14, s18)

def R_prlem1(ph, ps, ch, th, ta, et, h1, h2):
    s26 = R_biimprd(f"{ph}", f"{et}", f"{ch}", h1)
    s27 = R_adantld(f"{ph}", f"{ch}", f"{et}", f"{ps}", s26)
    s36 = R_pm2_21d(f"{ps}", f"{th}", f"{et}", h2)
    s37 = R_adantrd(f"{ps}", f"{th}", f"{et}", f"{ta}", s36)
    s38 = R_jaao(f"{ph}", f"∧{ps}{ch}", f"{et}", f"{ps}", f"∧{th}{ta}", s27, s37)
    return R_ex(f"{ph}", f"{ps}", f"→∨∧{ps}{ch}∧{th}{ta}{et}", s38)

@Theorem(4, "prlem2")
def R_prlem2(ph, ps, ch, th):
    s18 = R_simpl(f"{ph}", f"{ps}")
    s21 = R_simpl(f"{ch}", f"{th}")
    s22 = R_orim12i(f"∧{ph}{ps}", f"{ph}", f"∧{ch}{th}", f"{ch}", s18, s21)
    return R_pm4_71ri(f"∨∧{ph}{ps}∧{ch}{th}", f"∨{ph}{ch}", s22)

c.makePage("html/TrueLines.html")