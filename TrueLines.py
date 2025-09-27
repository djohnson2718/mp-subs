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

def R_bibi2i(ph, ps, ch, th, h1, h2):
    s8 = R_bitr4di(f"{ch}", f"{ph}", h1, f"{ch}", f"{ps}", h1)
