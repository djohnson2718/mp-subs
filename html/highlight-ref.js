types = ["antecedent", "mp-target", "sub-target"]

document.querySelectorAll("tbody tr").forEach(row => {
  row.addEventListener("mouseenter", () => {    
    for (t of types)
    {
        const refId = row.getAttribute(t);
        if (refId) {
            const refRow = document.getElementById(refId);
            if (refRow) refRow.classList.add(t);
        }
    }
  });

  row.addEventListener("mouseleave", () => {
    for (t of types)
    {
        const refId = row.getAttribute(t);
        if (refId) {
            const refRow = document.getElementById(refId);
            if (refRow) refRow.classList.remove(t);
        }
    }
  });
});