function [R, code] = random_projection(M, e)
    % M: matrix to reduce
    % e: 0 < e < 1, error, determines k | k << min(n, D)
    % D: see Li, P., Hastie, T. J., & Church, K. W. (2006, August). In Proceedings of the 12th ACM SIGKDD international conference on Knowledge discovery and data mining (pp. 287-296). ACM.
    [n, D] = size(M);
    k = ceil(9 * log(n) ./ (e.^2 - e.^3)),
    code = (sprand(D, k, 1 / (2 * sqrt(D))) & 1) - (sprand(D, k, 1 / (2 * sqrt(D))) & 1);
    R = (M * code) ./ sqrt(k);
