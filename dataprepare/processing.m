function processing(layer,nii)%example: processing(135,'D:\Research_Project\bio122\data\T1w_acpc_brain.nii')
nii = load_nii(nii, [], 1);
image=nii.img;

for i=1:311
    for j=1:260
        temp(i,j)=image(layer,i,j);
    end
end
temp=temp/max(max(temp))*255;
imagesc(uint8(temp));
end