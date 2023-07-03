clear

imgSize = [200,300];
imgPath = 'ProjectThumbnail';
imgDir = dir(imgPath);
imgDir(1:2) = [];

outPath = fullfile(imgPath, 'thumbnail');

for i=1:numel(imgDir)
    try
        im = imread(fullfile(imgPath, imgDir(i).name));
        im = imresize(im, imgSize);
        imwrite(im ,fullfile(outPath, imgDir(i).name));
    catch
    end
end