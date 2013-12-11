function N = nppmi(M)
    M = M ./ sum(sum(M));    % from counts to frequencies
    %tic, N = (M .* spfun(@(x) 1 ./ x, sum(M, 2) * sum(M)));toc, 
    tic, N = (diag(sparse(1./ sum(M, 2))) * M) * diag(sparse(1 ./ sum(M))); toc,
    %tic, N = (spdiags(1./ sum(M, 2), 0, size(M, 1), size(M,2)) * M) * spdiags(1 ./ sum(M)', 0, size(M, 1), size(M, 2)); toc,

    tic, N = spfun(@log2, N .* (N >= 1)); toc, % for PPMI and to preserve sparseness
    tic, N = N .* (-spfun(@(x) 1 ./ log2(x), M)); toc, % normalization
end