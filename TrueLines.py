from header import *

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

def R_syld(ph, ps, ch, th, h1, h2, h3):
    pass