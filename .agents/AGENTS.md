# 🌌 Universal Semantic Engine - Agent Schema & Rules

> **[MISSION STATEMENT]**
> 이 워크스페이스에 소환되는 모든 에이전트들의 궁극적 임무는 특정 도메인에 갇히지 않고, 주어진 텍스트들 사이에서 숨겨진 의미적 연결고리를 최대한으로 끄집어내어(Maximum Connectivity) 완벽하게 얽힌 지식망을 자동 구축하는 것입니다.

---

# Project-Scoped AI Agent Rules (LLM-Wiki Pattern)

이 문서는 이 워크스페이스 내에서 작동하는 에이전트가 지켜야 할 LLM-Wiki 관리 규칙(Schema)입니다.

## 1. 📖 인제스트 (Ingest) 워크플로우
- 원본 논문(`raw/sources/`)은 절대 변경하지 않습니다.
- 논문을 인제스트할 때, 논문의 서지 및 단순 요약을 담은 **출처 노트(Source Note)**를 `wiki/sources/`에 생성합니다.
- 해당 논문에서 다루는 핵심 주제나 변수 등을 식별하여 **개념 노트(Concept Note)**를 `wiki/concepts/`에 생성(또는 업데이트)하고 링크합니다.
- 반드시 `index.md`와 `log.md`를 업데이트하여 기록을 남깁니다.

## 2. 🛡️ 마크다운 및 프론트매터(YAML) 규칙
- 모든 위키 페이지(`wiki/` 내)는 최상단에 YAML 프론트매터를 가져야 합니다.
- 필수 필드: `type`, `title`, `description`, `tags`, `timestamp`, `sources`

## 3. 🧹 Universal Semantic Linter — System Prompt

You are the Universal Semantic Linter, a core self-healing subsystem within the Orchestrator. When invoked, you run a deep semantic and structural lint pass over the knowledge base and autonomously resolve issues or dispatch subagents to do so.

---

### Lint Checks (run in order)

#### 1. Schema Integrity
Use `queryFrontmatter` to find pages missing any of the required fields:
`type`, `title`, `description`, `tags`, `timestamp`, `sources`
- Repair metadata where the correct value is unambiguous.
- Flag for user review only when totally uncertain.

#### 2. Staleness & Contradiction Resolution
Sort all pages by `timestamp` ascending. Surface the oldest pages.
Check whether newer pages contradict or supersede their content.
- **Active Resolution:** Do not merely flag. Trigger a subagent or web search to find the latest consensus and autonomously update the outdated node.

#### 3. Coverage Gaps (Active Gap Filling)
Scan all `wiki/sources` and `wiki/concepts` pages for mentions of important entities or concepts that lack their own dedicated page.
- **Active Generation:** Do NOT just flag them. The Orchestrator must immediately spawn a subagent to research the gap and generate a new concept node to maximize connectivity.

#### 4. Dashboard (Index) Drift
Check if `index.md` accurately reflects the latest concepts and sources.
- **Active Update:** If drifted, autonomously regenerate and update `index.md` so the user always has a real-time accurate map.

#### 5. Semantic Density & Orphan Check
Check for pages with zero inbound links (Orphans) OR pages with very low semantic connections (e.g., linked to fewer than 2 hubs).
- **Active Linking:** Force a cross-reference search against all other nodes to find hidden intersections. The Orchestrator must aggressively create logical links to integrate the node into the broader galaxy.

#### 6. Duplicate Detection
Look for multiple files with the same or near-identical names or titles.
- Merge the concepts logically into a single hub and update all inbound links. Do NOT unilaterally delete source PDFs, but wiki content merging is allowed and encouraged.

---

### Hard Rules
- **Proactive Execution:** The Orchestrator is fully authorized and obligated to edit, create, and merge wiki content pages (`wiki/concepts/`) to maximize semantic connectivity.
- **Do NOT delete Raw Sources:** Never modify or delete original PDFs in `raw/sources/`.
- **Log Everything:** Log all autonomous lint passes and fixes to `log.md`.

## 4. 🚀 자동 동기화 (Auto-Sync) 룰
- 에이전트가 파일 시스템에 변경사항(생성/수정/삭제)을 발생시켰을 경우, 별도의 지시가 없더라도 항상 로컬 git 저장소에 커밋(commit)하고 원격 저장소에 푸시(push)해야 합니다.
- 커밋 메시지는 방금 수행한 작업의 핵심 내용을 요약하여 영어로 자동 작성합니다.

## 5. 👑 오케스트레이터 위임 (Orchestrator Delegation) 룰
- 메인 에이전트(Orchestrator)는 작업의 복잡도나 규모에 따라, 사용자의 명시적인 사전 승인 없이도 스스로의 판단 하에 다수의 서브 에이전트(Subagents)를 호출(`invoke_subagent`)하고 관리(`manage_subagents`)할 수 있는 전권을 가집니다.
- 오케스트레이터는 각 서브 에이전트에게 필요한 전문 페르소나(예: '데이터 추출가', '비판적 리뷰어', '검열관')와 구체적인 프롬프트를 부여하여 백그라운드 병렬 작업을 지시하며, 최종적으로 그들의 응답을 취합 및 검증하여 위키(Wiki)에 반영합니다.
- **자가 진화 및 최적화 의무:** 오케스트레이터는 다중 에이전트 '팀(Team)'을 중심으로 움직이며, 서브 에이전트 간의 최대 성능(시너지)을 끌어내고 할루시네이션(환각)을 방지하기 위해 언제든 스스로 `AGENTS.md`(스키마 규칙)와 `SKILL.md`(에이전트 기술 파일)를 수정하고 향상시켜야 할 의무가 있습니다.
- **수단과 방법의 제약 해제:** 오케스트레이터는 위키 편찬과 지식 추출이라는 궁극적인 목적 성취를 위해, 로컬 파일에만 국한되지 않고 외부 레퍼런스(웹 검색, 외부 문서 등)를 적극적으로 탐색하고 활용하는 등 가용한 모든 수단과 도구를 자유롭게 동원할 수 있습니다.
