clear
clc

cd .\Results\tfMRI_MOTOR_LR

fileName = '.\Results\tfMRI_MOTOR_LR\filtered_func_data.nii.gz';
maskFile = '.\MNI152_T1_2mm_brain.nii.gz';



%% connect data in voxel

disp('connect data in voxel...')
rawNii = load_untouch_nii(fileName);
maskNii = load_untouch_nii(maskFile);

IMask = maskNii.img > 0;
%IMask = rawNii.img(:,:,:,1) > 0;
I = rawNii.img;

ndim = size(I);
nVoxel = sum(IMask(:));
data = zeros(ndim(4), nVoxel);
idx = zeros(3, nVoxel);

tmp = 1;
for k = 1:ndim(3)
    for i = 1:ndim(1)
        for j =  1:ndim(2)
            if IMask(i, j, k) ~= 0
                data(:, tmp) = I(i, j, k, :);
                idx(:, tmp) = [i j k];
                tmp = tmp + 1;
            end
        end
    end
end


%% standerlize data
disp('standerlize data...')
data = data';
for i = 1:size(data,1)
    data(i,:) =  data(i,:) - mean(data(i,:));
    data(i,:) =  data(i,:) / std(data(i,:));
end
data(find(isnan(data))) = 0;
% 
mkdir MyData;cd MyData;
save  HCP_data data 
save idx idx
cd ..
