function srtotal = mvsim_full(m, sslice, it, k, p)
[rows, cols] =  size(m);
% find the real size of slice
slice = floor(cols / ceil(cols / sslice)),

% it seems logical to shuffle the attributes first!
m = m(:,randperm(cols));

srtotal = eye(rows);

I = [0:slice:cols, cols];
size(I,2) - 1,
for j = 1:it
    srinter = zeros(rows, rows);

    matlabpool('local', 7)
    parfor i = 1:size(I,2) - 1
        [j,i],
        MM = m(:, I(i) + 1:I(i+1));
        srinter = srinter + chisimk_full(MM, 1, srtotal, eye(size(MM, 2)), k, p);
    end
    matlabpool close


    srtotal = srinter ./ (size(I, 2) - 1);
end
