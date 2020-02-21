# optical_transfert_matrix
calculate_lens_systems



linear 2D lens and transfer

Raytracing in simple 2D approach via the optical transfer matrix. 
Why we need this: e.g. 2 lens system where the distance and focal length are a parameter. The optical transfermatrix can calculate the divergence of a beam (with an intial angle) passing through these lenses and propagating for another distance. 
(keyword: misaligned telescope for instance). 
The example case in the script calculates the outermost rays of a collminated beam passing through a long focal length
and hitting close to focus another lens with a significant smaller focal length (micro meter). This case happens in laser-plasma physics, where the laser is focused on a target, that turns into plasma and reflects the beam, but could be dented inwards from the 
so called hole-boring effect. Although this denting is in the nano-meter range this formed curved mirror has a diameter of the 
lasers' beamwaist - by this becomes a very short length focusing element. 
Linear approximation (this script) overestimates this effect, since in reality we deal with Gaussian spatial beam distributions
that lead to the so called beam-waist. (next step: gaussian beam and optical transfer matrix).
