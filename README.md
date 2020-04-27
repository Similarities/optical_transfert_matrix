# optical_transfert_matrix
calculate_lens_systems



linear 2D lens and transfer

Raytracing in simple 2D approach via the optical transfer matrix. 
https://en.wikipedia.org/wiki/Ray_transfer_matrix_analysis
Why we need this: e.g. 2 lens system where the distance and focal length are a parameter. The optical transfermatrix can calculate the divergence of a beam (with an intial angle) passing through these lenses and propagating for another distance. 
(keyword: misaligned telescope for instance). 
The example case in the script calculates the outermost rays of a collminated beam passing through a long focal length
and hitting close to focus another lens with a significant smaller focal length (micro meter). This case happens in laser-plasma physics, where the laser is focused on a target, that turns into plasma and reflects the beam, but could be dented inwards from the 
so called hole-boring effect. Although this denting is in the nano-meter range this formed curved mirror has a diameter of the 
lasers' beamwaist - by this becomes a very short length focusing element. 
Linear approximation (this script) overestimates this effect, since in reality we deal with Gaussian spatial beam distributions
that lead to the so called beam-waist. 

The calculation for Gaussian 2-lens system (actually, focused beam + one more lens) calculates via the q-vector
and the transfer matrix, first the new focal position (often referred as 'zn') and with this solves for the 
new beamwaist 'wnew'. The programm calculates this as a function of the lens position, close to focus (0 refers to the 
initial beamwaist position) and for a focal length that depends on the defocusing position. This case simulates a plasma lens
that is created by a target denting, from which the laser is then reflected. The Denting is assumed to depend on the
lasers intensity, and by this on the the beamwaist parameter w(z). This case can be identified with the conversation of the
wavefront-curvature in the emission of high harmonic radiation at defocused positions.
https://en.wikipedia.org/wiki/Gaussian_beam
(note: some parameters as Rayleighlength, wavefront curvature, beamwaist - focal length, divergence - are depending on each other 
for Gaussian beams)

In a last step the calculation is transferred to a high-harmonic beam, for one case that is discussed in literature: 
where without a second lens the wavelength is decreased by lambda/N (N = 1,2,3..., N), the minimum beamwaist is kept 
constant (w0) which leads to ~1/N dependency of the harmonic beamwaist at defocused positions (w(z,N)~1/N). The q-vector
changes and the new beamwaist for different defocusing position has a particular dependency on N and z- the defocusing 
parameter. 

As the HHG-topic is highly discussed in the literature, the published approaches by 'Vincenti et.al. 2013 Nat.Comm.' and a 
newer one is tested in the mathematica script for consistency of the above discribed case-study.
