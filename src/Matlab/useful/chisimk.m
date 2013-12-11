function [sr, sc] = chisimk(m, it, sr, sc, k, p)
    % If k == 1: chisim
    % k: norm
    % p: pruning, ratio
    % sr = speye(size(m, 1));
    % sc = speye(size(m, 2));

    m = m .^ k;
    for i=1:it
       [sr, sc] = inner_chisimk(m, sr, sc, k, p);  
    end
    
end

function [sr, sc] = inner_chisimk(m, sr, sc, k, p)
    if nnz(m) / numel(m) > 5 * 10^-3
        'Using dense matrices from now on',
        m = full(m);
        sr = full(sr);
        sc = full(sc);
    end
    sc_old = sc;
    sc = seteye(prune(normalize_chisimk(m' * sr     * m , k), p), 1);
    sr = seteye(prune(normalize_chisimk(m  * sc_old * m', k), p), 1);
end
  
function m = normalize_chisimk(m, k)
    m = m .^ (1 / k);
    d = diag(m);
    d(d == 0) = 1;
    dd = 1 ./ d;
    if issparse(m)
        m = m .* sqrt(sparse(dd * dd' .* (m > 0)));
    else
        m = m .* sqrt(dd * dd' .* (m > 0));
    end
end
