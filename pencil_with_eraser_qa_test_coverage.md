# Pencil with Eraser — Full QA Test Coverage

## 🔥 Test Goal
To validate that a pencil with an eraser performs reliably, safely, and consistently under real-world and extreme usage scenarios.

---

## ✍️ Functional Testing

### Writing
- Produces visible and consistent graphite marks
- Graphite color matches the expected specification
- Does not scratch or damage the writing surface during normal use
- Written text does not smudge during or immediately after writing under normal conditions
- Works on different paper textures
- Responds correctly to varying pressure levels


### Erasing
- Effectively removes graphite marks from the surface
- Does not excessively damage or tear the paper
- Allows re-writing after erasing
- Eraser does not crack, split, or break at the boundary between the eraser and its holder during normal use
- Eraser maintains structural integrity at the holder interface throughout its lifecycle

    #### Erasing → Edge Case / Contamination Testing
  - Test the eraser by first using it on a non-graphite substance (e.g., pen ink)
  - Verify that residual material does not smear or contaminate subsequent graphite erasing
  - Ensure that the eraser continues to remove graphite effectively after contact with other substances
  - Check that the paper is not stained or damaged due to contamination

### Construction
- Graphite core inside pencil 
- Eraser does not detach
- Body maintains structural integrity

---

## ✍️ Usability Testing

- Comfortable grip during long writing sessions
- Balanced weight distribution
- Easy transition between writing and erasing
- Suitable for left-handed and right-handed users

### Visibility
- Written text remains clearly visible under different lighting conditions
- Text is readable under bright light, low light, and artificial lighting
- Strong or direct lighting does not significantly reduce text readability due to glare or reflection

---

## ✍️ Maintenance & Replaceability
- Verify that the graphite core can be replaced without damaging the pencil
- Confirm that the eraser can be removed and replaced securely
- Replacement parts fit correctly and maintain original functionality
- Pencil continues to write and erase properly after replacing components

---

## ✍️ Performance Testing

- Writing quality over prolonged use
- Eraser effectiveness as it wears down
- Consistency after repeated sharpening

---

## ✍️ Load Testing

- Extended continuous writing
- Mixed high-frequency write/erase cycles

---

## ✍️ Stress Testing

### Mechanical Stress
- Excessive writing pressure
- Drops from desk height
- Moderate bending force

    #### Drop Test
  - Drop the pencil from desk height
  - Verify that the pencil body and graphite core remain intact
  - Verify that the graphite inside the pencil does not crack or become loose
  - Ensure the pencil can still be sharpened normally after a drop, without the graphite breaking repeatedly

### Environmental Stress
- Heat and cold exposure
- High humidity
- Long-term storage conditions

---

## ✍️ Safety (Security) Testing

- No sharp or hazardous edges
- Non-toxic materials
- No small detachable parts
- Safe eraser residue

---

## ✍️ Compatibility Testing

- Different paper qualities
- Various pencil sharpeners(sizes)
- Different usage styles

---

## ✍️ Reliability & Durability

- Long-term usage simulation
- Repeated sharpening cycles
- Full eraser lifecycle testing

---

## ✍️ Regression Testing

- Functionality after sharpening
- Functionality after stress exposure
- Verification of unchanged core behavior

---

## ✍️ Edge Cases

- Almost fully worn pencil
- Nearly depleted eraser
- Extremely light writing pressure
- Incorrect usage attempts

---

## ✍️ Summary

This test coverage demonstrates a structured QA mindset by applying classical testing methodologies to a simple physical object.
