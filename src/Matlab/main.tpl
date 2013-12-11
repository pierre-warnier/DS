M = mmread(XXX);
M = nppmi(M); % normalized positive point-wise mutual information
R = random_projection(M, .5);
S = R * R'; % cosine
S = prune(S, .99); % percentage => .01 density afterwards, very big save otherwise
mmwrite(YYY, S); % can be long, it is plain text, prune otherwise or find a way to zip on the fly or write to RAM file-system and then zip
